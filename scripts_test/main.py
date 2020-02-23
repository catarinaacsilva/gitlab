# coding=utf-8

import argparse
import logging



def main(args):
    create_usr(5)
    create_prj(5, 'usr0')
    # commit_prj(5, 'usr0', 'project_usr0_0') - Ver comentário abaixo
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gitlab user simulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', type=str, default='http://localhost:8000', help='Gitlab address')
    parser.add_argument('-t', type=str, default='e7NNphfyD6HKTbsBPygx', help='Gitlab private token')
    #parser.add_argument('-d', type=int, default=2, help='Minkowski distance of order p')
    args = parser.parse_args()
    main(args)
