function codebook = gen_vbs_cdb(k, vocabulary)
%=============================================================
%Input:
%           vocabulary         A m x d matrix represent all words in natural envoriment
%           k                        k is the number of clusters, which are used to generate a k x d codebook
%Output:
%           codebook          A k x d codebook generated by AK-means
%=============================================================
if(exist('codebook.mat', 'file'))
    load('codebook.mat');
    return;
end
dir_clt = './caltech-image-search-1.0/';
addpath (dir_clt);
dict_type = 'akmeans';
num_words = k;
num_iterations = 10;
num_trees = 2;
dict_params =  {num_iterations, 'kdt', num_trees};
codebook = ccvBowGetDict(vocabulary', [], [], num_words, 'flat', dict_type, [], dict_params);
save('codebook.mat', 'codebook');