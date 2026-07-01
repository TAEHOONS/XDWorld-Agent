---
description: 지도 내 다양한 형식의 배열 데이터를 사용하기 위한 API 입니다.
---

# Collection

> Module.Collection() API를 생성합니다.

```javascript
var data_array = new Module.Collection();
```

## properties

| Name  | Type   | Description        |
| :---- | :----- | :----------------- |
| count | number | 등록된 총 배열 수. |

## Function

### GetCount() → number

> 등록된 총 배열 수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 등록된 총 배열 수.

{% endtab %}
{% tab title="Template" %}

```javascript
var array = new Module.Collection();
var count = array.GetCount();
```

{% endtab %}
{% endtabs %}

### extend(elements) → void

> 배열에 새로운 데이터 리스트를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type  | Description      |
| :------ | :---- | :--------------- |
| element | array | 추가 데이터 리스트. |

{% endtab %}
{% tab title="Template" %}

```javascript
var array = new Module.Collection();
var items = [
    new Module.JSVector3D(126.77599416643791, 35.02714918251881, 34.293371013365686),
    new Module.JSVector3D(126.78374897355015, 35.03318059967435, 35.54886215366423),
    new Module.JSVector3D(126.79212321528658, 35.03203801070689, 25.686076117679477),
    new Module.JSVector3D(126.79408620811664, 35.019259090964134, 29.999966450035572)
];
array.extend(items);
```

{% endtab %}
{% endtabs %}

### add(element) → number

> 배열에 새로운 데이터를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description  |
| :------ | :----- | :----------- |
| element | object | 추가 데이터. |

-   Return
    -   number: 등록된 총 배열 수.

{% endtab %}
{% tab title="Template" %}

```javascript
var movePosition = new Module.Collection();
movePosition.add(new Module.JSVector3D(126.77599416643791, 35.02714918251881, 34.293371013365686));
movePosition.add(new Module.JSVector3D(126.78374897355015, 35.03318059967435, 35.54886215366423));
movePosition.add(new Module.JSVector3D(126.79212321528658, 35.03203801070689, 25.686076117679477));
movePosition.add(new Module.JSVector3D(126.79408620811664, 35.019259090964134, 29.999966450035572));
```

{% endtab %}
{% endtabs %}

### update(index, item) → void

> 입력 변수값(index) 인덱스에 해당하는 값을 변경합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| :---- | :----- | :----------- |
| index | number | 배열 인덱스.  |
| item  | object | 변경할 데이터. |

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### switch(index1, index2) → void

> 각 입력 변수값(index1, index2) 인덱스에 해당하는 값을 서로 교환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description  |
| :----- | :----- | :----------- |
| index1 | number | 배열 인덱스 1. |
| index2 | number | 배열 인덱스 2. |

{% endtab %}
{% tab title="Template" %}

```javascript
var array = new Module.Collection();
array.switch(1, 3); // 1번 인덱스의 데이터와 3번 인덱스의 데이터를 교환
```

{% endtab %}
{% endtabs %}

### pop() → object

> 배열의 첫 번째 요소를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   object: 배열의 첫 번째 데이터.

{% endtab %}
{% tab title="Template" %}

```javascript
var array = new Module.Collection();
array.switch(1, 3); // 1번 인덱스의 데이터와 3번 인덱스의 데이터를 교환
```

{% endtab %}
{% endtabs %}

### clear()

> 등록된 배열 데이터를 삭제합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var array = new Module.Collection();
array.clear();
```

{% endtab %}
{% endtabs %}

### item(index) → object

> 등록된 배열에 해당되는 값을 반환합니다.
>
> 입력 변수값(index) 인덱스에 해당하는 값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| :---- | :----- | :----------- |
| index | number | 배열 인덱스. |

-   Return
    -   object: 인덱스 번호에 해당하는 데이터.

{% endtab %}
{% tab title="Template" %}

```javascript
var array = new Module.Collection();
/* add data */
var data = array.item(1); // 1번째 인덱스 데이터
```

{% endtab %}
{% endtabs %}