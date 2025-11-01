"""deploy_dashboard.py

Placeholder script to demonstrate how you might automate publishing to Power BI Service.
Implement OAuth and use the Power BI REST API or `powerbiclient` for real deployments.
"""
import argparse
from etl.utils.helpers import load_config


def main(config_path: str):
    cfg = load_config(config_path)
    # TODO: implement Power BI publish using service principal
    print('Deploying dashboard (placeholder). Update this script with real auth and API calls.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', dest='config', default='config.yaml')
    args = parser.parse_args()
    main(args.config)
