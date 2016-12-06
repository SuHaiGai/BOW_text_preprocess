%create a n*1 matrix to describe a 256 label (0,1)
n = 100;
label = ones(n,1);
vec = load('zhangxiaobeiVlad.mat')
vec_doc=vec.vec_doc;
[i, j] = size(vec_doc);
matdata = [vec_doc(:,1:j) label];

% % read data file
% if strfind(input_filename,'.mat')
%     matdata = importdata(input_filename);
% elseif strfind(input_filename,'.txt')
%     matdata = textread(input_filename) ;
% elseif strfind(input_filename,'.csv')
%     matdata = csvread(input_filename);
% end;



[row,col] = size(matdata);
f = fopen('zhangxiaobeiVlad.arff','wt');
% if (f < 0)
%     error(sprintf('Unable to open the file %s',arff_filename));
%     return;
% end;
fprintf(f,'%s\n',['@relation ','zhangxiaobeiVlad.arff']);

for i = 1 : col - 1
st = ['@attribute att_',num2str(i),' numeric'];
fprintf(f,'%s\n',st);
end;

% save the last row info of the headfile 
floatformat = '%.16g';

Y = matdata(:,col);
uY = unique(Y); %  get label type
st = ['@attribute label {'];
for j = 1 : size(uY) - 1
    st = [st sprintf([floatformat ' ,'],uY(j))];
end;
st = [st sprintf([floatformat '}'],uY(length(uY)))];
fprintf(f,'%s\n\n',st);

% start to save data
labelformat = [floatformat ' '];
fprintf(f,'@data\n');
for i = 1 : row
    Xi = matdata(i,1:col-1);
    s = sprintf(labelformat,Y(i));
    s = [sprintf([floatformat ' '],[; Xi]) s];
    fprintf(f,'%s\n',s);
end;
fclose(f);


