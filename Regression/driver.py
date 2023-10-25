from dataloader import Dataloader


def main():
    data_loader = Dataloader()

    data_loader.read_yaml_config('config.yaml')
    data_loader.read_csv_file('all_August_2019.csv')
    print('YAML configuration')
    print(data_loader.config)

    for row in data_loader.data:
        print(row)


if __name__ == "__main__":
    main()
