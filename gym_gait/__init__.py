from gym.envs.registration import register

register(
    id='HalfCheetah-gait-test',
    entry_point='gym_gait.envs.half_cheetah_gait_test:HalfCheetahEnv',
)
register(
    id='HalfCheetah-gait-v0',
    entry_point='gym_gait.envs.half_cheetah_gait_v0:HalfCheetahEnv',
)