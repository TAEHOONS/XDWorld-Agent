---
description: 텍스처로 사용되는 아이콘 개체입니다. [JSSymbol](./jssymbol.md) 클래스 객체로 등록하여 사용하며, 각 아이콘은 등록 시 고유 명칭으로 설정됩니다. 고유 명칭은 중복하여 등록할 수 없습니다.
---

# JSIcon

> Module.getSymbol API를 생성합니다.

```javascript
var symbol = Module.getSymbol();
symbol.insertIcon(/*..parameter*/);
var icon = symbol.getIcon("ID");
```

## Function

### getId() → string

> 객체의 고유 명칭을 반환 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   string: 객체 설명 문자열이 성공적으로 반환.
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var strKey = object.getId();
```

{% endtab %}
{% endtabs %}

### getReferenceCount() → number

> JSIcon을 참조 중인 오브젝트 수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number(0 ~ ): 참조된 오브젝트 수.
    -   -1: 반환 실패.
    -   실패 조건
        -   JSIcon이 정상적으로 생성되지 않은 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var icon = Module.getSymbol().getIcon("mapIcon");
var refCount = icon.getReferenceCount();
```

{% endtab %}
{% endtabs %}
