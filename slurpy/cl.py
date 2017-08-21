import slurpy

import datetime

NOW = datetime.datetime.now()


def query_jobs():
    jobs = slurpy.get_job_df(partition='cpu',
                             end_time=NOW,
                             period=datetime.timedelta(days=1))
    jobs['Jobs'] = 1

    print(jobs.head())

    print('Most recent start time: {}'.format(jobs['Start'].max()))
    print('Most recent submit time: {}'.format(jobs['Submit'].max()))

    print(jobs.groupby('State').sum())

    return 0


def query_nodes():
    nodes = slurpy.get_node_df(partition='cpu')
    nodes['NODES'] = 1
    del nodes['MEMORY']
    print(nodes.groupby('STATE').sum())

    return 0
