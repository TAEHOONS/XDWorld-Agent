---
description: 지도 내 3차원 막대 그래프 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSBarGraph3D

Module.createBarGraph3D() API를 생성합니다.

```javascript
var object = Module.createBarGraph3D("ID");
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

### create(position, size) → boolean

> Create a 3D graph object.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                          |
| :------- | :---------------------------------- | :----------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 그래프 생성 좌표 (경도, 위도, 고도). |
| size     | [JSSize3D](../core/jssize3d.md)     | 크기(너비, 높이 설정).               |

-   Return
    -   true: 생성 성공.
    -   false : 생성 실패.
-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### insertColumn(name, label, color) → boolean

> 그래프 컬럼 정보를 추가합니다..

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description                       |
| :---- | :---------------------------- | :-------------------------------- |
| name  | string                        | column 구분 명칭.                 |
| label | string                        | column 명칭 (그래프 하단부 표시). |
| color | [JSColor](../core/jscolor.md) | 그래프 바 색상.                   |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### insertRow(name, label) → boolean

> 그래프 레코드 정보를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                       |
| :---- | :----- | :-------------------------------- |
| name  | string | 레코드 구분 명칭.                 |
| label | string | 레코드 이름 (그래프 하단부 표시). |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setAnimationSpeed(speed) → boolean

> 그래프 바 상승 애니메이션 속도 설정.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                                     |
| :---- | :----- | :---------------------------------------------- |
| speed | number | 바 상승 애니메이션 속도 (0.1~1.0 사이 값 설정). |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setColumnTextBackgroundColor(key, color) → boolean

> 그래프 바 하단부 Column 문자열 배경 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description                              |
| :---- | :---------------------------- | :--------------------------------------- |
| key   | string                        | 텍스트 색상을 변경하고자 하는 Column 키. |
| color | [JSColor](../core/jscolor.md) | 문자열 배경 색상.                        |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setColumnTextColor(key, outColor, fillColor) → boolean

> 그래프 바 하단부 Column 라벨 배경 색상을 설정..

{% tabs %}
{% tab title="Information" %}

| Name      | Type                          | Description                              |
| :-------- | :---------------------------- | :--------------------------------------- |
| key       | string                        | 텍스트 색상을 변경하고자 하는 Column 키. |
| outColor  | [JSColor](../core/jscolor.md) | 텍스트 외곽 색상.                        |
| fillColor | [JSColor](../core/jscolor.md) | 텍스트 채움 색상.                        |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var graph = Module.createBarGraph3D("Graph");
//...
var outlineColor = new Module.JSColor(255, 255, 255);
var fillColor = new Module.JSColor(0, 0, 0);
graph.setColumnTextColor("Column0", outlineColor, fillColor);
```

{% endtab %}
{% endtabs %}

### setData(name, label, data) → boolean

> 지정한 Column, Row에 해당하는 그래프 데이터를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description       |
| :---- | :----- | :---------------- |
| name  | string | column 구분 명칭. |
| label | string | Row 구분 명칭.    |
| data  | number | 그래프 데이터.    |

-   Return
    -   true : 추가 성공.
    -   false : 추가 실패.
-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setUnitText(unit) → boolean

> 그래프 높이 축 단위 표시 텍스트 설정합니다..

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| :--- | :----- | :----------- |
| unit | string | 단위 문자열. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setValueRange(min, max, value) → boolean

> 그래프 높이 축의 최소, 최대 값 설정.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description      |
| :---- | :----- | :--------------- |
| min   | number | 높이 축 최소 값. |
| max   | number | 높이 축 최대 값. |
| value | number | 눈금 표시 간격.  |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function createGraph 참조.
    -   [Sandbox_3D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_3d)

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
