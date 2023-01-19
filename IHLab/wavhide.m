clc;
clear;
fid = fopen('high_ganrao.wav', 'r');
oa = fread(fid, inf, 'uint16');
fclose(fid);

f = fopen('high_Chinese48000.wav', 'r');
[msg, len_total] = fread(f,'ubit1');
fclose(f);

% 防止嵌入消息大于载体
n = length(oa) - 44;
if len_total > n
    error('嵌入消息量过大');
end

% 保存秘密信息的前44字节的文件格式说明
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
% 嵌入
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

disp(len); % body的长度


