#!/usr/bin/env python3

def clean_rewards(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if 'Reward' in line:
                lines.remove(line)
    with open(filename, 'w') as f:
        for line in lines:
            if 'Quest' in line:
                f.write(line)
                f.write('\n')
            else:
                f.write(line)
                f.write('\n\n')


clean_rewards('rewards_list.txt')
