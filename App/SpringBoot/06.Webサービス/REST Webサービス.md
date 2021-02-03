# REST Webサービス

<!-- MarkdownTOC -->

- 実装例
    - 基本的な実装
- アノテーション
    - クラスにつけるアノテーション
        - `@RestController`
        - `@Controller`
    - メソッドにつけるアノテーション
        - `@GetMapping("UIRパス")`
        - `@PathVariable`
        - `@ResponseStatus(HttpStatus.~)`
        - `@RequestMapping(value="URIパス", method=RequestMethod.{GET,POST})`
        - `@ResponseBody`
        - `@RequestParam`

<!-- /MarkdownTOC -->


## 実装例

```java
package com.example.api;

// import ...

@RestController
@RequestMapping("api/customers")
public class CustomerRestController {
    @Autowired
    CustomerService customerService;

    // 顧客全件取得
    @GetMapping
    List<Customer> getCustomers() {
        List<Customer> customers = customerService.findAll();
        return customers;
    }

    // 顧客1件取得
    @GetMapping(path="{id}")
    Customer getCustomer(@PathVariable Integer id) {
        Customer customer = customerService.findOne(id);
        return customer;
    }
}
```

### 基本的な実装
```java
package com.example.api;

// import ...

@RestController
@RequestMapping("api/example")
public class ExampleRestController {

    @GetMapping  // curl -XGET http://example.com/api/example
    List<Example> getExamples() {
        // READ処理
    }

    @GetMapping(path = "{id}")  // curl -XGET http://example.com/api/example/12
    Example getExample(@PathVariable Integer id) {
        // READ処理
    }

    @PostMapping  // curl -XPOST http://example.com/api/example/ -i -H "Content-Type:application/json" -d "{"exampleName": "hoge", ...}"
    @ResponsesStatus(HttpStatus.CREATED) // API正常時のHTTPレスポンスを設定
    Example postExample(@RequestBody Example example) {
        // CREATE処理
    }

    @PutMapping(path = "{id}")
    Example putExample(@PathVariable Integer id, @RequestBody Example example) {
        // UPDATE処理
    }

    @DeleteMapping(path = "{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    void deleteExample(@PathVariable Integer id) {
        // DELETE処理
    }
}
```

---
## アノテーション

### クラスにつけるアノテーション
#### `@RestController`

 - 定義場所 : クラス定義の前
 - 意味 :
    - そのクラスが「RESTコントローラー」であることを示す
    - アクセスした側にテキストを出力するだけのもの

```java
package com.example.demo.HelloWorld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
    @GetMapping("/helloworld")
    public String HelloWorld() {
        return "Hello Taiyo!";
    }
}
```

#### `@Controller`

 - 定義場所 : クラス定義の前
 - 意味 : テンプレートを利用してHTMLページをレンダリングし、表示する



### メソッドにつけるアノテーション

#### `@GetMapping("UIRパス")`

 - 定義場所 : メソッド定義の前
 - 意味 : この”アドレス”にGETアクセスしたら、このメソッドを実行する

```java
package com.example.demo.HelloWorld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
    @GetMapping("/helloworld")
    public String HelloWorld() {
        return "I'm Taiyo!";
    }
}
```

#### `@PathVariable`
引数などの値を`@GetMapping`などのpath属性で指定されたプレースホルダの値にします。

 - プレースホルダ名と引数名は一致させる必要がある

#### `@ResponseStatus(HttpStatus.~)`
応答のステータスコードを指定する。

#### `@RequestMapping(value="URIパス", method=RequestMethod.{GET,POST})`

 - 意味 : この”アドレス”にアクセスしたら、このメソッドを実行する

```java
package com.example.demo.HelloWorld;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
    @RequestMapping(value="/helloworld", method = RequestMethod.GET)
    public String HelloWorld() {
        return "I'm Taiyo!";
    }
}
```

#### `@ResponseBody`

 - 定義場所 : メソッド定義の前
 - 意味 : レスポンス(サーバからクライアントへ返送される内容)をオブジェクトで設定できるようにする

#### `@RequestParam`

 - 定義場所 : メソッドの引数の前
 - 意味 :

```java
メソッド名(@RequestParam("input,textareaタグのname属性の値”)パラメータの型 変数名, ...)
```