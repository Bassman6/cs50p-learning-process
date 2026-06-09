# from tiwtter import shorten


# def main():
#     test_shorten()


# def test_shorten():
#     try: 
#         assert shorten("tiwtter") == '0'
#     except AssertionError:
#         print("fail")

#     return 

# if __name__ == "__main___":

#     main()

from tiwtter import shorten

def test_shorten():
    # 没有任何拦截，错了就让它尽情报错
    assert shorten("tiwtter") == '0'  # 这次你再运行，必定爆红 Fail