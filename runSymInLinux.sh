#! /bin/bash
#
# Run experiment in a Linux system
#  Pass the path to the experiment directory
experimentDir=$1

echo "Creating aneurysm and vessel geometry..."
python constructAneuGeom.py \
    --experiment_dir $experimentDir

echo "Creating initial stent..."
python constructInitFD.py \
    --experiment_dir $experimentDir \
    --stent_pos outer

echo "Deploying stent..."
python deployStent.py \
    --experiment_dir $experimentDir \
    --stent_pos outer

python mergeMesh.py --experiment_dir $experimentDir
