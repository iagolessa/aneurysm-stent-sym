import argparse
import trimesh
import json, os

def main(dir_path:str):
    # Create results directory if not existent
    resultsPath = os.path.join(dir_path, "results")

    if not os.path.exists(resultsPath):
        os.makedirs(resultsPath)

    experiment_number = os.path.basename(
                            os.path.normpath(dir_path)
                        ).split("_")[-1]

    vessel=trimesh.load("{}/results/vessel_EX{}.stl".format(dir_path,experiment_number))
    deployed_stent=trimesh.load("{}/results/deployed_outer_stentEX{}.stl".format(dir_path,experiment_number))
    combined = trimesh.util.concatenate([vessel,deployed_stent])
    combined.export(file_obj="{}/results/stented1x_vessel_EX{}.stl".format(dir_path,experiment_number))

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '--experiment_dir',
        type=str,
        default='./',
        help='Path to experiment directory'
    )
    args=parser.parse_args()
    directory_path=args.experiment_dir
    main(directory_path)


