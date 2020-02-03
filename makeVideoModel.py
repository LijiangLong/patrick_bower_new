from Modules.FileManagers.FileManager import FileManager as FM
import subprocess
import pdb


fm_obj = FM()
pdb.set_trace()
a = fm_obj.localOrganizedLabeledClipsDir
b = fm_obj.local3DVideosDir
#fm_obj.downloadAnnotationData('LabeledVideos')

#subprocess.run(['python3', 'Modules/MachineLearning/3D_resnet.py', '--data', fm_obj.localOrganizedLabeledClipsDir, '--results', fm_obj.local3DVideosDir])


