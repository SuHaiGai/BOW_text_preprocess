%vocabulary = rand(100000, 150);
vocabulary = load('convert.wiki.zh.text.vector');

k = 2^8;
codebook = gen_vbs_cdb(k, vocabulary);

% file
edit_A = load('aixiaoke_01.txt');
%BoW
vec_A = gen_edt_vec(edit_A, codebook);
%VLAD
vec_vlad_A = gen_edit_vlad(edit_A, codebook);
edit_B = rand(500, 150);
%BoW
vec_B = gen_edt_vec(edit_B, codebook);
%VLAD
vec_vlad_B = gen_edit_vlad(edit_B, codebook);