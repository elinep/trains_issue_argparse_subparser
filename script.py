from argparse import ArgumentParser
from trains import Task

def build_parser():
    parser = ArgumentParser()
    parser.add_argument("--global_param0", type=int, default=1)
    parser.add_argument("--global_param1", default=int(1))

    sub_program_subparser = parser.add_subparsers(dest="sub_program")
    program_subparser = sub_program_subparser.add_parser("program")
    program_subparser.add_argument('--specific_param0', type=int, default=1)
    program_subparser.add_argument('--specific_param1', default=int(1))
    return parser

if __name__ == '__main__':
    # create task
    task = Task.init(project_name='argparser_issue', task_name='test')
    # set manualy requirements, auto detection will timeout
    task._update_requirements("trains")

    parser = build_parser()
    args = parser.parse_args()
    print("parsed arguments:")
    print(args)


# python script.py --global_param0 2 --global_param1 2 program --specific_param0 2 --specific_param1 2
# TRAINS_TASK_ID=916dcba419a74b68bf1e0d986aacc1ef python script.py