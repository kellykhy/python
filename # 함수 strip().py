# 함수 strip()

example = "000aaa000bbb00"
strip_ex = example.strip('0')  #왼쪽, 오른쪽에서 제거
lstrip_ex = example.lstrip('0') #왼쪽에서 제거
rstrip_ex = example.rstrip('0') #오른쪽에서 제거

print("original string :", example)
print("strip result :", strip_ex)
print("lstrip result :", lstrip_ex)
print("rstrip result :", rstrip_ex)