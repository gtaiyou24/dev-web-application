# Strategyパターン

Strategy とは英語で「戦略」を意味する言葉です。Strategy パターンを利用することで、戦略の切り替えや追加が簡単に行えるようになります。

普通にプログラミングしていると、メソッドの中に溶け込んだ形でアルゴリズムを実装してしまうことがよくあります。if 文などで分岐させることでアルゴリズムを変更するような方法です。Strategy パターンでは、戦略の部分を意識して別クラスとして作成するようにしています。戦略x部分を別クラスとして作成しておき、戦略を変更したい場合には、利用する戦略クラスを変更するという方法で対応します。Strategy パターンを利用することで、メソッドの中に溶け込んだ形のアルゴリズムより柔軟でメンテナンスしやすい設計となります。

##