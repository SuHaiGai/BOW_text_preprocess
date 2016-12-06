%vocabulary = rand(100000, 150);

k = 2^8;
if ~exist('codebook.mat', 'file')
    vocabulary = load('convert.wiki.zh.text.vector');
end
% vocabulary = load('convert.wiki.zh.text.vector');
codebook = gen_vbs_cdb(k, vocabulary);

% traditional BOW
% fnames = dir(fullfile('/home/zhouyang/Downloads/CriticalCategorization/matlab_vet_input/muweier_vecInput', '*.txt'));
% vec_doc = zeros(length(fnames), k);
% for iter = 1:length(fnames)
%     edit_t = load(fullfile('/home/zhouyang/Downloads/CriticalCategorization/matlab_vet_input/muweier_vecInput', fnames(iter).name));
%     vec_t = gen_edt_vec(edit_t, codebook);
%     vec_doc(iter, :) = vec_t;
%     
% end
% 
% save('muweier.mat', 'vec_doc');

% VLAD
fnames = dir(fullfile('/home/zhouyang/Downloads/CriticalCategorization/matlab_vet_input/zhangxiaobei_vecInput', '*.txt'));
vec_doc = zeros(length(fnames), k*150);
for iter = 1:length(fnames)
    edit_t = load(fullfile('/home/zhouyang/Downloads/CriticalCategorization/matlab_vet_input/zhangxiaobei_vecInput', fnames(iter).name));
    vec_t = gen_edit_vlad(edit_t, codebook);
    vec_doc(iter, :) = vec_t';
    
end

save('zhangxiaobeiVlad.mat', 'vec_doc');



% edit_A = load('aixiaoke_01.txt');
% %BoW
% vec_A = gen_edt_vec(edit_A, codebook);
% %VLAD
% vec_vlad_A = gen_edit_vlad(edit_A, codebook);
% edit_B = rand(500, 150);
% %BoW
% vec_B = gen_edt_vec(edit_B, codebook);
% %VLAD
% vec_vlad_B = gen_edit_vlad(edit_B, codebook);

