from eulerTools import is_palindrome

ans = 0

for n in range(1000001):
    if is_palindrome(str(n)):
        if is_palindrome(bin(n)[2:]):
            ans += n

print(ans)