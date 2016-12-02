__author__ = 'Matjaz'
DEFAULTS = dict()
DEFAULTS['excitation_type'] = 'impulse'
DEFAULTS['channel_types'] = ['f'] + ['a']*13
# TODO: Implement auto! (MAX value taken)
DEFAULTS['samples_per_channel'] = 10000
DEFAULTS['nodes'] = [0,0]
DEFAULTS['directions'] = ['+x']*13
DEFAULTS['trigger_level'] = 5
DEFAULTS['pre_trigger_samples'] = 30
DEFAULTS['exc_channel'] = 0
DEFAULTS['resp_channels'] = [1]*13
DEFAULTS['exc_window'] = 'Force:0.01'
DEFAULTS['resp_window'] = 'Exponential:0.01'
DEFAULTS['channel_delay'] = [0.]*14
DEFAULTS['weighting'] = 'None'
DEFAULTS['n_averages'] = 10
DEFAULTS['fft_len'] = 'auto'
DEFAULTS['pre_trigger_samples'] = 30
DEFAULTS['zero_padding'] = 0
DEFAULTS['save_time_history'] = False
DEFAULTS['roving_type'] = 'Ref. node'
DEFAULTS['selected_model_id'] = 1