---
description: 지도 내 포인트 그래프 객체를 생성 및 설정하기 위한 API 입니다.
---

# CJSPointGraph

> Module.createPointGraph() API를 생성합니다.

```javascript
var object = Module.createPointGraph("ID");
```

## Function

### create(position, size) → boolean

> 포인트 그래프 객체를 생성하니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                  |
| :------- | :---------------------------------- | :--------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 중심 좌표(경도, 위도, 고도). |
| size     | [JSSize3D](../core/jssize3d.md)     | 그래프 크기.                 |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Point Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_point)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

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

### insertData(x, y, z, value) → boolean

> 포인트 그래프를 구성하는 데이터를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description |
| :---- | :----- | :---------- |
| x     | number | x축 위치.   |
| y     | number | y축 위치.   |
| z     | number | z축 위치.   |
| value | number | 데이터 값.  |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Point Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_point)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### insertLegend(value, color) → boolean

> 포인트 그래프를 구성하는 범례를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| :---- | :---------------------------- | :---------- |
| value | number                        | 범례 값.    |
| color | [JSColor](../core/jscolor.md) | 범례 색상.  |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Point Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_point)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setAxisRange(axis, min, max, interval) → boolean

> 포인트 그래프를 구성하는 각 축의 범위 및 눈금, 간격 가시화를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description                         |
| :------- | :----- | :---------------------------------- |
| axis     | number | 축 타입(0 : X축, 1 : Y축, 2 : Z축). |
| min      | number | 축 최소 값.                         |
| max      | number | 축 최대 값.                         |
| interval | number | 그래프 눈금 표시 간격.              |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Point Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_point)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPointLineVisible(type) → boolean

> 포인트 그래프와 지형을 연결하는 직선 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                        |
| :--- | :------ | :------------------------------------------------- |
| type | boolean | <p>true: 직선 가시화.<br>false: 직선 비가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Point Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_point)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getDescription(), setDescription(desc) → string

> 객체에 대한 설명을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| ---- | ------ | ------------ |
| desc | string | 설명 문자열. |

-   Return
    -   string: 객체 설명 문자열이 성공적으로 반환.
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var strDesc = object.getDescription();
// ... or ...
object.setDescription("First Object.");
```

{% endtab %}
{% endtabs %}

### getName(), setName(name) → string

> 객체 이름을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| name | string | 객체 이름.  |

-   Return
    -   string: 객체 이름을 성공적을 반환
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var objName = object.getName();
// ... or ...
object.setName("MyObject");
```

{% endtab %}
{% endtabs %}

### getVisible(), setVisible(visible) → boolean

> 객체의 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                        |
| ------- | ------- | -------------------------------------------------- |
| visible | boolean | <p>true: 객체 가시화.<br>false: 객체 비가시화.</p> |

-   Return
    -   true: 객체 가시화 상태.
    -   false: 객체 비가시화 상태.

{% endtab %}
{% tab title="Template" %}

```javascript
var objName = object.getName();
// ... or ...
object.setVisible(true);
```

{% endtab %}
{% endtabs %}
