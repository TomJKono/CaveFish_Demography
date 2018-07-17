#!/usr/bin/env python
"""Implement a Python class that runs a dadi model."""

import dadi
import pylab
from ..Optim import dadi_custom
import numpy
import math


class DemoModel(object):
    """A class to hold data and methods for running a demographic model in dadi.
    Will store the model function, and joint SFS data."""

    def __init__(self, sfs, model, popnames, output):
        """Initialization function. Sets the model name and function, path to
        input data, and the output filename."""
        self.sfs = self.load_sfs(sfs)
        self.modelname = model
        # Make an extrapolating version of the function
        self.modelfunc = dadi.Numerics.make_extrap_log_func(
            self.set_model_func(model))
        self.params = self.set_parameters()
        self.popnames = popnames
        self.output = '_'.join(popnames + [output, model]) + '.txt'
        self.figout = '_'.join(popnames + [output, model]) + '_Comp.pdf'
        return

    def load_sfs(self, sfs):
        """Parse the dadi SFS file and return it as a Spectrum object. Dadi will
        do basic checking of the spectrum, but we will be more thorough."""
        try:
            fs = dadi.Spectrum.from_file(sfs)
        except:
            print 'The spectrum file you provided is not valid!'
            exit(1)
        return fs

    def set_model_func(self, model):
        """Given a model name, set the function that has to be called to run
        that model. This should be safe because we restrict the user input for
        the models at the argument parsing stage."""
        if model == 'SI':
            import cavefish_dadi.Models.si
            return cavefish_dadi.Models.si.si
        elif model == 'SC':
            import cavefish_dadi.Models.sc
            return cavefish_dadi.Models.sc.sc
        elif model == 'IM':
            import cavefish_dadi.Models.im
            return cavefish_dadi.Models.im.im
        elif model == 'AM':
            import cavefish_dadi.Models.am
            return cavefish_dadi.Models.am.am
        elif model == 'SC2M':
            import cavefish_dadi.Models.sc2m
            return cavefish_dadi.Models.sc2m.sc2m
        elif model == 'IM2M':
            import cavefish_dadi.Models.im2m
            return cavefish_dadi.Models.im2m.im2m
        elif model == 'AM2M':
            import cavefish_dadi.Models.am2m
            return cavefish_dadi.Models.am2m.am2m
        else:
            return None

    def set_parameters(self):
        """Set the parameters for the function, depending on the model being
        run. Also set the bounds for the optimization."""
        params = {}
        if self.modelname == 'SI':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after splot
            # Ts: Time from split to present, in 2*Na generation units
            names = ['N1', 'N2', 'Ts']
            values = [1, 1, 1]
            upper_bounds = [20, 20, 10]
            lower_bounds = [0.01, 0.01, 0]
        elif self.modelname == 'IM':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after split
            # m21: Migration from 1 to 2 (2*Na*mm21)
            # m12: Migration from 2 to 1 (2*Na*m12)
            # Ts: Time from split to present, in 2*Na generations
            names = ['N1', 'N2', 'm21', 'm12', 'Ts']
            values = [1, 1, 1, 1, 1]
            upper_bounds = [20, 20, 20, 20, 10]
            lower_bounds = [0.01, 0.01, 0, 0, 0]
        elif self.modelname == 'AM':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after split
            # m21: Migration from 1 to 2 (2*Na*mm21)
            # m12: Migration from 2 to 1 (2*Na*m12)
            # Tam: Time from end of anc migration to split, in 2*Na gens
            # Ts: Time from split to present, in 2*Na generations
            names = ['N1', 'N2', 'm21', 'm12', 'Tam', 'Ts']
            values = [1, 1, 1, 1, 0.1, 1]
            upper_bounds = [20, 20, 20, 20, 2, 10]
            lower_bounds = [0.01, 0.01, 0, 0, 0, 0]
        elif self.modelname == 'SC':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after split
            # m21: Migration from 1 to 2 (2*Na*mm21)
            # m12: Migration from 2 to 1 (2*Na*m12)
            # Ts: Time from split to secondary contact, in 2*Na generations
            # Tsc: Time from secondary contact to presesnt, in 2*Na gens
            names = ['N1', 'N2', 'm21', 'm12', 'Ts', 'Tsc']
            values = [1, 1, 1, 1, 1, 0.1]
            upper_bounds = [20, 20, 20, 20, 10, 2]
            lower_bounds = [0.01, 0.01, 0, 0, 0, 0]
        elif self.modelname == 'IM2M':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after split
            # m21: Migration from 1 to 2 (2*Na*mm21)
            # m12: Migration from 2 to 1 (2*Na*m12)
            # mi21: Migration from 1 to 2 in "islands" (2*Na*mi21)
            # mi12: Migration from 1 to 2 in "islands" (2*Na*mi12)
            # Ts: Time from split to present, in 2*Na generations
            # p: Porpotion of genome evoloving in "islands"
            names = ['N1', 'N2', 'm21', 'm12', 'mi21', 'mi12', 'Ts', 'p']
            values = [1, 1, 5, 5, 0.5, 0.5, 1, 0.5]
            upper_bounds = [20, 20, 30, 30, 5, 5, 10, 0.95]
            lower_bounds = [0.01, 0.01, 0, 0, 0, 0, 0, 0.05]
        elif self.modelname == 'AM2M':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after split
            # m21: Migration from 1 to 2 (2*Na*mm21)
            # m12: Migration from 2 to 1 (2*Na*m12)
            # mi21: Migration from 1 to 2 in "islands" (2*Na*mi21)
            # mi12: Migration from 1 to 2 in "islands" (2*Na*mi12)
            # Tam: Time from end of anc migration to split, in 2*Na gens
            # Ts: Time from split to present, in 2*Na generations
            # p: Porpotion of genome evoloving in "islands"
            names = ['N1', 'N2', 'm21', 'm12', 'mi21', 'mi12', 'Tam', 'Ts', 'p']
            values = [1, 1, 5, 5, 0.5, 0.5, 0.1, 1, 0.5]
            upper_bounds = [20, 20, 30, 30, 5, 5, 2, 10, 0.95]
            lower_bounds = [0.01, 0.01, 0, 0, 0, 0, 0, 0, 0.05]
        elif self.modelname == 'SC2M':
            # N1: Pop 1 size after split
            # N2: Pop 2 size after split
            # m21: Migration from 1 to 2 (2*Na*mm21)
            # m12: Migration from 2 to 1 (2*Na*m12)
            # mi21: Migration from 1 to 2 in "islands" (2*Na*mi21)
            # mi12: Migration from 1 to 2 in "islands" (2*Na*mi12)
            # Ts: Time from split to secondary contact, in 2*Na generations
            # Tsc: Time from secondary contact to presesnt, in 2*Na gens
            # p: Porpotion of genome evoloving in "islands"
            names = ['N1', 'N2', 'm21', 'm12', 'mi21', 'mi12', 'Ts', 'Tsc', 'p']
            values = [1, 1, 5, 5, 0.5, 0.5, 1, 0.1, 0.5]
            upper_bounds = [20, 20, 30, 30, 5, 5, 10, 2, 0.95]
            lower_bounds = [0.01, 0.01, 0, 0, 0, 0, 0, 0, 0.05]
        params['Names'] = names
        params['Values'] = values
        params['Upper'] = upper_bounds
        params['Lower'] = lower_bounds
        return params

    def infer(self, niter, reps):
        """Inference function. This borrows heavily from the callmodel()
        function in 'script_inference_anneal2_newton.py' from SEA lab."""
        # Start containers to hold the optimized parameters
        self.p_init = []
        self.hot_params = []
        self.cold_params = []
        self.opt_params = []
        self.theta = []
        self.mod_like = []
        self.opt_like = []
        self.aic = []
        # Get the sample sizes from the SFS
        sample_sizes = self.sfs.sample_sizes
        # Generate the points of the grid for the optimization
        grid = 50
        # Apply mask
        # Calculate the model SFS
        mod_sfs = self.modelfunc(self.params['Values'], sample_sizes, grid)
        # Calculate the likelihood of the data given the model SFS that we just
        # generated
        mod_like = dadi.Inference.ll_multinom(mod_sfs, self.sfs)
        # Start with hot annealing, then cold annealing, then BFGS
        r = 0
        while r < reps:
            p_init = dadi.Misc.perturb_params(
                self.params['Values'],
                fold=1,
                lower_bound=self.params['Lower'],
                upper_bound=self.params['Upper'])
            # Get some hot-optimized parameters
            p_hot = dadi_custom.optimize_anneal(
                p_init,
                self.sfs,
                self.modelfunc,
                grid,
                lower_bound=self.params['Lower'],
                upper_bound=self.params['Upper'],
                maxiter=niter,
                Tini=100,
                Tfin=0,
                learn_rate=0.005,
                schedule="cauchy")
            p_cold = dadi_custom.optimize_anneal(
                p_hot,
                self.sfs,
                self.modelfunc,
                grid,
                lower_bound=self.params['Lower'],
                upper_bound=self.params['Upper'],
                maxiter=niter,
                Tini=50,
                Tfin=0,
                learn_rate=0.01,
                schedule="cauchy")
            p_bfgs = dadi.Inference.optimize_log(
                p_cold,
                self.sfs,
                self.modelfunc,
                grid,
                lower_bound=self.params['Lower'],
                upper_bound=self.params['Upper'],
                maxiter=niter)
            self.p_init.append(p_init)
            self.hot_params.append(p_hot)
            self.cold_params.append(p_cold)
            self.opt_params.append(p_bfgs)
            opt_sfs = self.modelfunc(p_bfgs, sample_sizes, grid)
            opt_like = dadi.Inference.ll_multinom(opt_sfs, self.sfs)
            # Estimate theta
            self.theta.append(dadi.Inference.optimal_sfs_scaling(opt_sfs, self.sfs))
            # And calculate the AIC
            aic = 2 * len(self.params) - 2 * opt_like
            self.mod_like.append(mod_like)
            self.opt_like.append(opt_like)
            self.aic.append(aic)
            r += 1
        # Set these as class variables for printing later
        self.model_sfs = opt_sfs
        return

    def summarize(self, locuslen):
        """Summarize the replicate runs and convert the parameters estimates
        into meaningful numbers."""
        # First, calculate the mean of the parameter estimates from each
        # of the replicates
        hot_means = []
        for r_t in zip(*self.hot_params):
            v = [x for x in r_t if not math.isnan(x)]
            hot_means.append(sum(v)/len(v))
        cold_means = []
        for r_t in zip(*self.cold_params):
            v = [x for x in r_t if not math.isnan(x)]
            cold_means.append(sum(v)/len(v))
        bfgs_means = []
        for r_t in zip(*self.opt_params):
            v = [x for x in r_t if not math.isnan(x)]
            bfgs_means.append(sum(v)/len(v))
        theta_mean = sum(self.theta) / len(self.theta)
        # Then, convert the parameters into meaningful values
        #   the theta estimate is 4*Na*u*L
        anc_ne = theta_mean / (4 * 3e-9 * locuslen)
        #   Then, the parameters are scaled by that. Population sizes are scaled
        #   by theta (4Na), and times and migration rates are given in units of
        #   2N.
        scaled_params = []
        for name, val in zip(self.params['Names'], bfgs_means):
            if name.startswith('N'):
                scaled_params.append(val * anc_ne)
            elif name.startswith('m'):
                scaled_params.append(val /(anc_ne * 2))
            elif name.startswith('T'):
                scaled_params.append(val * anc_ne * 2)
            else:
                scaled_params.append(val)
        # Write these values into the class data
        self.hot_mean = hot_means
        self.cold_mean = cold_means
        self.bfgs_mean = bfgs_means
        self.theta_mean = theta_mean
        self.Na = anc_ne
        self.scaled_params = scaled_params
        return


    def write_out(self, niter, locuslen):
        """Write some output summaries for the dadi runs."""
        try:
            handle = open(self.output, 'w')
        except OSError:
            print 'Error, you do not have permission to write files here.'
            extit(1)
        # First, write the pop names
        handle.write('#Pop 1: ' + self.popnames[0] + '\n')
        handle.write('#Pop 2: ' + self.popnames[1] + '\n')
        # Then write the run parameters
        handle.write('#Model: ' + self.modelname + '\n')
        handle.write('#Max iterations: ' + str(niter) + '\n')
        # Then write some model summaries
        handle.write('#Data Likelihoods: ' + ' '.join([str(s) for s in self.mod_like]) + '\n')
        handle.write('#Optimized Likelihoods: ' + ' '.join([str(s) for s in self.opt_like]) + '\n')
        handle.write('#AIC: ' + ' '.join([str(s) for s in self.aic]) + '\n')
        handle.write('#LocusLem: ' + str(locuslen) + '\n')
        handle.write('#4*Na*u*L: ' + str(self.theta_mean) + '\n')
        handle.write('#Na: ' + str(self.Na) + '\n')
        for name, val in zip(self.params['Names'], self.scaled_params):
            towrite = '#' + name + ': ' + str(val) + '\n'
            handle.write(towrite)
        # Then a table of the parameters that were found
        handle.write('Iteration\t' + '\t'.join(self.params['Names']) + '\n')
        handle.write('Initial\t' + '\t'.join([str(s) for s in self.params['Values']]) + '\n')
        # Write the perturbed parameters
        for index, vals in enumerate(self.p_init):
            name = 'Perturbed_' + str(index) + '\t'
            handle.write(name + '\t'.join([str(s) for s in vals]) + '\n')
        # And the hot annealed values
        for index, vals in enumerate(self.hot_params):
            name = 'Hot_Anneal_' + str(index) + '\t'
            handle.write(name + '\t'.join([str(s) for s in vals]) + '\n')
        # And the cold annealed values
        for index, vals in enumerate(self.cold_params):
            name = 'Cold_Anneal_' + str(index) + '\t'
            handle.write(name + '\t'.join([str(s) for s in vals]) + '\n')
        # And the BFGS parameters
        for index, vals in enumerate(self.opt_params):
            name = 'BFGS_' + str(index) + '\t'
            handle.write(name + '\t'.join([str(s) for s in vals]) + '\n')
        # And the final params
        handle.write('Hot_Mean\t' + '\t'.join([str(s) for s in self.hot_mean]) + '\n')
        handle.write('Cold_Mean\t' + '\t'.join([str(s) for s in self.cold_mean]) + '\n')
        handle.write('BFGS_Mean\t' + '\t'.join([str(s) for s in self.bfgs_mean]) + '\n')
        handle.flush()
        handle.close()
        return

    def plot(self, vmin, vmax, resid_range=None,
             pop_ids=None, residual='Anscombe'):
        """Plot the comparison between the data and the chosen model. This is a
        copy-paste with some modification from the
        dadi.Plotting.plot_2d_comp_Poisson function."""
        # Scale the model SFS to the data SFS
        sc_mod = dadi.Inference.optimally_scaled_sfs(self.model_sfs, self.sfs)
        # Start a new figure, and clear it
        f = pylab.gcf()
        pylab.clf()

        ax = pylab.subplot(2,2,1)
        dadi.Plotting.plot_single_2d_sfs(self.sfs, vmin=vmin, vmax=vmax,
                           pop_ids=self.popnames, colorbar=False)
        ax.set_title('Data')

        ax2 = pylab.subplot(2,2,2, sharex=ax, sharey=ax)
        dadi.Plotting.plot_single_2d_sfs(sc_mod, vmin=vmin, vmax=vmax,
                           pop_ids=self.popnames, extend='neither')
        ax2.set_title('Model')

        resid = dadi.Inference.Anscombe_Poisson_residual(sc_mod, self.sfs,
                                              mask=vmin)
        if resid_range is None:
            resid_range = max((abs(resid.max()), abs(resid.min())))

        ax3 = pylab.subplot(2,2,3, sharex=ax, sharey=ax)
        dadi.Plotting.plot_2d_resid(resid, resid_range, pop_ids=self.popnames,
                      extend='neither')
        ax3.set_title('Residuals')

        ax = pylab.subplot(2,2,4)
        flatresid = numpy.compress(numpy.logical_not(resid.mask.ravel()), 
                                   resid.ravel())
        ax.hist(flatresid, bins=20, normed=True)
        ax.set_title('Residuals')
        ax.set_yticks([])
        pylab.tight_layout()
        f.savefig(self.figout, bbox_inches='tight')
        return
