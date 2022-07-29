import requests

result = requests.get("https://api.ipify.org/?format=json").content
s = result.decode("utf-8");
ans = "";
for i in range(len(s)):
    if(s[i]!='{'and s[i]!='}'):
        ans += s[i];
list = ans.split(':');
ans1 =" ";
for i in range(len(list[1])):
    if list[1][i]!='"' :
        ans1 += list[1][i];
        
print(ans1);
