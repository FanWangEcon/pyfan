'''
Created on Dec 4, 2017

@author: fan
'''

import logging
import numpy as np

logger = logging.getLogger(__name__)


class UtilityMultiNomial():
    """
    each_j_indirect_utility:
        N by J matrix

    N is the number of individuals (unique states)
    J is the number of choices

    N might be 0
    """

    def __init__(self, scale_coef=1):
        """
        Parameters
        ---------
        scale_coef : float
            Usually this is not an important paramter, it is usually 1, but 
            based on my reading for nonlinear logit, need, could have a scale
            coefficient, could test this out, anyway, this is to be estimated
            potentially if the indirect utility component is nonlinear
            
        """
        '''
        Train Page 40 about scale parameter
        in linear in parameter logit, when rescaling linear parameters
        scale coefficient does not matter. But in nonlinear, they do. 
        '''
        self.scale_coef = scale_coef

    def prob_denominator(self, all_J_indirect_utility):
        '''
        if: 
                all_J_indirect_utility/self.scale_coef = -598.66/0.75
            then: 
                prob_denominator = exp(-598.66/0.75) = 0.0
            then: 
                sum(prob_denominator) = 0
            then:
                np.exp(all_J_indirect_utility/self.scale_coef)/prob_denominator_tile = INVALID
        so there must be some minimal level for the division here. in terms of scaling
        '''

        #         all_J_indirect_utility/self.scale_coef

        #         prob_denominator = np.sum(np.exp(all_J_indirect_utility/self.scale_coef), axis=1)
        prob_denominator = np.sum(np.exp(all_J_indirect_utility), axis=1)

        return prob_denominator

    #         np.exp(-598.66)
    def prob_j(self, all_J_indirect_utility, prob_denominator=None):
        if (prob_denominator is None):
            prob_denominator = self.prob_denominator(all_J_indirect_utility)

        choice_J_count = np.shape(all_J_indirect_utility)[1]
        logger.debug('choice_J_count:\n%s', choice_J_count)

        prob_denominator_tile = np.transpose(
            np.tile(prob_denominator, (choice_J_count, 1)))

        logger.debug('all_J_indirect_utility:\n%s', all_J_indirect_utility)
        logger.debug('self.scale_coef:\n%s', self.scale_coef)
        logger.debug('prob_denominator_tile:\n%s', prob_denominator_tile)

        #         each_j_prob = np.exp(all_J_indirect_utility/self.scale_coef)/prob_denominator_tile
        each_j_prob = np.exp(all_J_indirect_utility) / prob_denominator_tile

        logger.debug('each_j_prob:\n%s', each_j_prob)
        return each_j_prob

    def expected_u_integrate_allj(self, prob_denominator):
        '''
        'see Train discussion on consumer surplus and logit'
        'Need to check the reference that Train cites to make sure this integration applies in my case, should derive it myself'
        If one option has much higher utility, 
        and if variance is low, integrated utility is linear in this option, 
        in fact they are equal 
        '''
        optiV_Exp7 = np.log(prob_denominator)
        return optiV_Exp7

    def get_outputs(self, all_J_indirect_utility):
        all_J_indirect_utility = all_J_indirect_utility / self.scale_coef

        brk_low = -600
        gap = 100
        base = (brk_low - gap)
        too_low_idx = [(all_J_indirect_utility) <= brk_low]
        all_J_indirect_utility[too_low_idx] = base + (
                1 / (brk_low + 1 - all_J_indirect_utility[too_low_idx]) ** (1 / 4)) * 100

        brk_high = 600
        base = (brk_high + gap)
        too_high_idx = [(all_J_indirect_utility) >= brk_high]
        all_J_indirect_utility[too_high_idx] = base - (
                1 / (all_J_indirect_utility[too_high_idx] - brk_high + 1) ** (1 / 4)) * 100

        logger.debug('all_J_indirect_utility:\n%s', all_J_indirect_utility)
        prob_denominator = self.prob_denominator(all_J_indirect_utility)
        logger.debug('prob_denominator:\n%s', prob_denominator)
        each_j_prob = self.prob_j(all_J_indirect_utility, prob_denominator)
        optiV_Exp7 = self.expected_u_integrate_allj(prob_denominator)

        return each_j_prob, optiV_Exp7
