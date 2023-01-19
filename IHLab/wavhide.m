clc;
clear;
fid = fopen('high_ganrao.wav', 'r');
oa = fread(fid, inf, 'uint16');
fclose(fid);

f = fopen('high_Chinese48000.wav', 'r');
[msg, len_total] = fread(f,'ubit1');
fclose(f);

% ��ֹǶ����Ϣ��������
n = length(oa) - 44;
if len_total > n
    error('Ƕ����Ϣ������');
end

% ����������Ϣ��ǰ44�ֽڵ��ļ���ʽ˵��
head = zeros(1, 44 * 8);
for i = 1 : 44 * 8
    head(i)=msg(i);
end

len = len_total - 44 * 8;
body = zeros(1, len);
for i = 1 : len
    body(i) = msg(i + 44 * 8);
end

j = 45;
% Ƕ��
M = oa;
for i = 45 : 45 + len -1
    M(i) = bitset(M(i), 1, body(i - 44));
end

fid = fopen('lsb_high.wav', 'wb');
fwrite(fid, M, 'uint16');
fclose(fid);

fid = fopen('head.wav', 'wb');
fwrite(fid, head, 'ubit1');
fclose(fid);

disp(len); % body�ĳ���


