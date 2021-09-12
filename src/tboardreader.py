#!/usr/bin/env python3
import argparse
import os
import warnings

import pandas as pd

from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


class tensorboardReader():       
    def convert_log2df(self, events, tag_req):
        """This method reads the tensorboard event file and extracts required
            tag
        Args:
            events (str): Path for tensorboard event file
            tag_req (str): Required tag to extract from event file(default:'all')

        Returns:
            [list]: List of extracted tag values
            [list]: List of tags
        """
        
        size_guidance = {
            'COMPRESSED_HISTOGRAMS': 0,
            'IMAGES': 0,
            'AUDIO': 0,
            'SCALARS': 0,
            'HISTOGRAMS': 0,
        }
        logs = []
        tags = ['step']
        # event accumulator to read the file
        try:
            event_acc = EventAccumulator(events, size_guidance)
            event_acc.Reload()
            avail_tags = event_acc.Tags()['scalars']
            for index, each_tag in enumerate(avail_tags):
                # Extract all values in the tag
                if each_tag == tag_req:
                    logs = self.extract_tag(event_acc, each_tag)
                    tags.append(each_tag)
                    break
                elif tag_req.lower() == 'all':
                    values = self.extract_tag(event_acc, each_tag)
                    tags.append(each_tag)
                    if index == 0:
                        logs.append(values[0])
                        logs.append(values[1])
                    else:
                        logs.append(values[1])
        except Exception:
            print('Invalid event file')
        if len(logs) == 0:
            warnings.warn('Invalid tag continuing with next file')
        print(tags)
        return logs, tags

    def extract_tag(self, event_acc, tag):
        """
        Extract the specified tags value and step
        
        Args:
            event_acc: Event accumulator object haolding log file values
            tag (str): Tag to extract the value
        
        Returns:
            [list] : List of all the values in the tag
        """
        event_list = event_acc.Scalars(tag)
        vals = list(map(lambda x: x.value, event_list))
        step = list(map(lambda x: x.step, event_list))
        return [step, vals]

    def save_csv(self, data, filename, verbose):
        csv_name = 'tensor_board_logdata_'+filename.split('/')[-1]+'.csv'
        if verbose:
            print('Saving the file as {}'.format(csv_name))
        data.to_csv(csv_name, index=False)

    def run(self, args):
        """
        This method extracts values from all log files in path and saves
        
        Args:
            args: Parser object

        Returns:
            None
        """
        file_list = []
        # Read all the files in the path
        for (dir, _, files) in os.walk(args.path):
            file_list += [os.path.join(dir, filename) for filename in files]
        if len(file_list) == 0:
            raise ValueError('No files found in current path')
        elif args.verbose:
            print('Found {} files in current path'.format(len(file_list)))
        logdata = []
        # Enumerate each file
        for index, each_file in enumerate(file_list):
            if args.verbose:
                print('Reading log file-{} --> {}'.format(index+1, each_file))
            # Extract the values
            values, tags = self.convert_log2df(each_file, args.tag)
            logdata.append(values)
            logdata_df = pd.DataFrame(values).T
            logdata_df.columns = tags
            # Save as CSV
            if args.save:
                self.save_csv(logdata_df, each_file, args.verbose)


def parse_cmd():
    """
    Method to create argument parser
    
    Args:
        None
    """
    parser = argparse.ArgumentParser(description='Tensorboard log reader')
    parser.add_argument(
        '--path',
        default=None,
        required=True,
        help='Path of the tensorboard log file'
    )
    parser.add_argument(
        '--tag',
        default='all',
        help='Required tag in log file, Default to read all tags'
    )
    parser.add_argument(
        '--save',
        action='store_true',
        default=True,
        help='For saving the values as a csv file'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        default=False,
        help='Plot the read tag values against step'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        default=True,
        help='Print the steps'
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cmd()
    reader = tensorboardReader()
    reader.run(args)