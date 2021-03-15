# @CreateTime : 2021/3/11
# @Author : sunx
import os
import pickle

# res_path = 'logs/hico-det_final/results/test_bbox_results_flip_final.pkl'
# res = pickle.load(open(res_path, 'rb'))
# a = 1

os.chdir('eval_hico')
os.system('matlab -nodesktop -nosplash -r "Generate_detection ' + '../logs/hico-det_final/results/hico-det_final_flip_final' + '/;quit;"')
os.chdir('..')

