fid = fopen('high_mix.wav', 'r');
oa = fread(fid, inf, 'uint16');

f = fopen('head.wav', 'r');
[head, len] = fread(f,'ubit1');
fclose(f);

m = oa;
n = 4560934;
disp(size(m));
for i = 1 : n - 44
    w(i) = bitget(m(44 + i), 1);
end
fclose(fid);

len_total = len + n - 44;
full = zeros(1, len_total);
for i = 1 : len
    full(i) = head(i);
end
for i = len+1 : len_total
    full(i) = w(i-len);
end

fid = fopen('lsb_secret.wav', 'wb');
fwrite(fid, full, 'ubit1');
fclose(fid);
disp('ok');