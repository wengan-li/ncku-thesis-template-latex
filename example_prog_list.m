function [mean, stdev] = stats(x)
n = length(x); %% 中文註釋，以雙百分號起頭; 但註釋裏不要含有 \LaTeX{} 的命令字串，如半形括號、底線，除非你要產生對應的的效果，如下標。程式行太長，可以自動斷行。
mean = sum(x) / n; % normal comment in English
stdev = sqrt(sum( (x-mean) .^ 2 / (n-1) ));
printf('The mean = %g\n');