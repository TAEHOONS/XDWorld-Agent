---
description: 지도 내 3d 그물형 격자 그래프 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSSurfaceGraph

> Module.createSurfaceGraph() API를 생성합니다.

```javascript
var object = Module.createSurfaceGraph("ID");
```

## Function

### create(position, size) → boolean

> 3d 그물형 격자 그래프 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                   |
| :------- | :---------------------------------- | :---------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 중심 좌표 (경도, 위도, 고도). |
| size     | [JSSize3D](../core/jssize3d.md)     | 크기.                         |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
-   Sample
    -   the createGraph function.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

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

### insertAxisPoint(axis, value) → boolean

> 3d 그물형 그래프를 구성하는 x,y 축의 눈금값을 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                                  |
| :---- | :----- | :------------------------------------------- |
| axis  | number | <p>Axis type.<br>0: X-axis.<br>1: Y-axis</p> |
| value | number | Tick value.                                  |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### insertLegend(value, color) → boolean

> 3d 그물형 그래프 객체를 구성하는 범례와 색상을 설정합니다..

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description  |
| :---- | :---------------------------- | :----------- |
| value | number                        | 범례 구간값. |
| color | [JSColor](../core/jscolor.md) | 범례 색상값. |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setAnimationSpeed(speed) → boolean

> 3d 그물형 그래프 객체 애니메이션 재생 속도를 설정합니다..

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description        |
| :---- | :----- | :----------------- |
| speed | number | 속도 (0.1 and 1.0) |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setData(x, y, value) → boolean

> 3d 그물형 그래프 객체를 구성하는 데이터를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description |
| :---- | :----- | :---------- |
| x     | number | x축 좌표.   |
| y     | number | x축 좌표.   |
| value | number | 데이터.     |

-   Return
    -   true : 추가 성공.
    -   false : 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setValueRange(min, max, interval) → boolean

> 3d 그물형 그래프 객체의 높이 축 범위를 설정합니다.
>
> 입력 변수값(interval)은 0.0 보다 큰값이 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description     |
| :------- | :----- | :-------------- |
| min      | number | 축 최소값.      |
| max      | number | 축 최대값.      |
| interval | number | 눈금 표시 간격. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setUnitText(text) → boolean

> 3d 그물형 그래프 객체의 높이 축 단위 표시 문자열을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| :--- | :----- | :---------- |
| text | string | 단위 명칭.  |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_Surface Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_surface)

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
