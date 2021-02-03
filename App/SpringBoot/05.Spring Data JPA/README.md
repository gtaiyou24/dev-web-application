# Spring Data JPA

## JPAとは

 - 「JPA」: Java標準の「O/Rマッパー」に関する仕様
 - 実装ライブラリとして、「Hibernate」「EclipseLink」が有名
 - 特徴
    - 「Javaオブジェクト」と「データベースに格納されているデータ」とのマッピング機能
    - 「データベース」への「CRUD処理」をカプセル化した「API」
    - 「Javaオブジェクト」を検索するための「クエリ言語」(JPQL)
    - データベース製品の差異を「JPA」で吸収

## 環境

 - dependencies:
    - JPA
    - Lombok

---
## 実装
### エンティティクラスの実装
```java
package com.example.domain;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistenct.*;

@Entity  // JPAのエンティティであることを示す
@Table(name="customers")  // エンティティに対応するターブル名を指定.デフォルトでは、「テーブル名=クラス名」
@Data
@NoArgsConstructor   // JPAの仕様でエンティティクラスには引数のないデフォルト・コンストラクタを作る必要がある
@AllArgsConstructor
public class Customer {
    @Id  // エンティティの主キーであるフィールドに付ける
    @GeneratedValue  // 主キーが自動採番されることを@GeneratedValueアノテーションを付けて示す
    private Integer id;
    @Column(nullable=false)  // フィールドに@Columnアノテーションを付けて、該当するDBのカラムに対する「名前」や「制約」など設定
    private String firstName;
    @Column(nullable=false)
    private String lastName;
}
```

### リポジトリクラスの実装
**JpaRepositoryインターフェイス**<br>
JpaRepositoryインターフェイスを実装したクラスを作成すると、以下のようなメソッドが自動的に生成されます。

| メソッド | 説明 |
|:-------:|:----|
| `findAll()` | 全行検索を行います |
| `findOne(id)` | 指定したidの行を検索します |
| `save()` | 引数で指定したエンティティクラスで挿入あるいは更新を行います |
| `delete(id)` | 指定したidの行を削除します |

```java
package com.example.repository

import com.example.domain.Customer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CustomerRepository extends JpaRepository<Customer, Integer> {
}
```

 - 「インターフェイス」さえあれば実行時に「実行クラス」が生成されるので、冗長なプログラムを記述する必要がない

使用例)
```java
@Autowired
CustomerRepository customerRepository;

// ...
//
// customerRepository.findAll().forEach(System.out::println);
```

### 独自処理を実装
`JpaRepository`には定義されていない検索処理などをしたい場合は、継承したインターフェイスに対応するメソッドをJPQLで記述します。

> **JPQL(Java Persistence Query Language)とは**<br>
> データベースを検索、更新などを行うクエリ言語で、SQLがテーブルを対象としたクエリ言語であるのに対して、エンティティクラスを対象としたクエリ言語です。
>
> - JPA仕様で定義される
> - データベースベンダごとのSQL文法の違いを吸収
>
> 以下のJPQLの例のSELECTの後の`x`は、Customerエンティティクラスの別名で、これでCustomerエンティティクラスのフィールドすべてという意味になります。
```sql
SELECT x FROM Customer x ORDER BY x.firstName, x.lastName
```

実装例) Customerを「名前の昇順で取得するメソッド」を`CustomerRepository`に追加
```java
package com.example.repository

import com.example.domain.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface CustomerRepository extends JpaRepository<Customer, Integer> {
    @Query("SELECT x FROM Customer x ORDER BY x.firstName, x.lastName")
    List<Customer> findAllOrderByName();
}
```
`@Query`アノテーションを付けて、「JPQL」を記述。
