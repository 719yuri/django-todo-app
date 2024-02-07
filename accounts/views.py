from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    template_name='accounts/login.html',
    redirect_authenticated_user='True',

#2/7めも　とりあえずこのauthe~~をauthe n ticated にしたけど変わらず。
#ちな動画(56)ではN抜け、でも問題なさそうだった…動画の他のとこではN入れてるし、
#地の文でも入ってるから入れるに越したことはないでしょう。

#追記。タイプエラーとは型がおかしいということ（使えない変数使っちゃってるとか、成立してないみたいな。
#️今回はタプルじゃダメと言われてる。タプル＝複数の要素が決まった順番？に並んだ値「オブジェクト」のこと。
#んで、タプルじゃなくてstrとか他の使ってねって言われてる。っぽい。
#んで、/accounts/login/に問題があるらしい。タイプエラーなのだから紐づいてないとかそういうんではなさそう？
#ログインと同時に作ったログアウトは問題なかったのになあ。。二つの違いってViewsに切り分けてルーティングしたかどうかくらい。
#次見てみるときはhttps://prograshi.com/language/python/python-tuple/を見てみようかな。知らない間に勝手にタプルとかこわ。
#

