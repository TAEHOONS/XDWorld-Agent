---
description: 지도 내 2차원 좌표 배열과 관련된 기능을 관리하기 위한 API 입니다.
---

# JSVec2Array

> Module.JSVec2Array() API를 생성합니다

```javascript
var vec_array = new Module.JSVec2Array();
```

## Function

### clear()

> 등록된 벡터 목록을 삭제합니다

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
vectorList.clear();
```

{% endtab %}
{% endtabs %}

### count() → number

> 등록된 벡터 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 등록 된 총 벡터 개수.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
// ...
vectorList.count();
```

{% endtab %}
{% endtabs %}

### get(index) → [JSVector2D](../core/jsvector2d.md)

> 등록된 벡터 정보를 반환합니다.
>
> 입력 변수값(index) 인덱스에 해당하는 값을 반한합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| :---- | :----- | :----------- |
| index | number | 인덱스 번호. |

-   Return
    -   [JSVector2D](../core/jsvector2d.md)): 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
var vector = vectorList.get(2);
```

{% endtab %}
{% endtabs %}

### pop() → [JSVector2D](../core/jsvector2d.md)

> 벡터 목록 중 마지막 데이터를 반환합니다.
>
> 반환 후 마지막 벡터는 벡터 목록에서 삭제 됩니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector2D](../core/jsvector2d.md): 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
//...
var lastVector = vectorList.pop();
```

{% endtab %}
{% endtabs %}

### push(element) → number

> 새로운 벡터를 추가한다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                                | Description      |
| :------ | :---------------------------------- | :--------------- |
| element | [JSVector2D](../core/jsvector2d.md) | 2차원 벡터 등록. |

-   Return
    -   number: 등록된 벡터 개수 반환.

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
var newVector = new Module.JSVector2d(100.0, 150.0);
vectorList.push(newVector);
```

{% endtab %}
{% endtabs %}

### pushXY(dX, dY) → number

> 입력 변수값(dX, dY)으로 새로운 벡터 객체를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| :--- | :----- | :---------- |
| dX   | number | X축 좌표계. |
| dY   | number | Y축 좌표계. |

-   Return
    -   number: 등록된 벡터 개수 반환.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
vectorList.pushXY(100.0, 120.0);
```

{% endtab %}
{% endtabs %}

### set(index, vec)

> 등록 벡터 데이터를 재 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                | Description     |
| :---- | :---------------------------------- | :-------------- |
| index | number                              | 인덱스 번호.    |
| vec   | [JSVector2D](../core/jsvector2d.md) | 재설정 벡터 값. |

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
//...
var newVector = new Module.JSVector2D(130.22, 149.3);
vectorList.set(5, newVector);
```

{% endtab %}
{% endtabs %}

### setXY(index, dX, dY)

> 입력 변수값(index, dX, dY)으로 벡터 객체를 수정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description      |
| :---- | :----- | :--------------- |
| index | number | 인덱스 번호.     |
| dX    | number | X축 위치 좌표값. |
| dY    | number | Y축 위치 좌표값. |

{% endtab %}

{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
//...
vectorList.setXY(5, 130.22, 149.3);
```

{% endtab %}
{% endtabs %}

### shift()

> 벡터 목록의 첫번쨰 벡터를 반환하고 두번째 벡터 목록의 첫번쨰 위치로 한칸씩 앞으로 이동한다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector2D](../core/jsvector2d.md): 반환성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var vectorList = new Module.JSVec2Array();
//...
var lastVector = vectorList.shift();
```

{% endtab %}
{% endtabs %}

### pointToString() → string

> 포인트 리스트를 문자열로 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   string: "x1,y1,x2,y2,x3,y3,..."

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getBoundary() → object

> 입력된 좌표 리스트의 Boundary를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   min: [JSVector2D](../core/jsvector2d.md)
    -   max: [JSVector2D](../core/jsvector2d.md)

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### toJSVec3Array() → [JSVec3Array](../core/jsvec3array.md)

> 입력된 좌표리스트의 jsvec3array를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVec3Array](../core/jsvec3array.md): 반환성공.

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}