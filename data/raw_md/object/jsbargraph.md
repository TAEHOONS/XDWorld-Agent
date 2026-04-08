---
description: 지도 내 2차원 막대 그래프 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSBarGraph

> Module.createBarGraph() API를 생성합니다.

```javascript
var object = Module.createBarGraph("ID");
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

### create(position, size, type) → boolean

> 2차원 막대 그래프 객체를 생성합니다.
>
> 입력 변수값(type)에 따른 시각화 방법이 변경됩니다.
>
> -   0: 수평 그래프 형태.
> -   1: 수직 그래프 형태.

{% tabs %}
{% tab title="Infomation" %}

| Name     | Type                                | Description                                        |
| :------- | :---------------------------------- | :------------------------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 그래프 생성 좌표 (경도, 위도, 고도) 기준은 중하단. |
| size     | [JSSize2D](../core/jssize2d.md)     | 크기(너비, 높이 설정).                             |
| type     | number                              | 그래프 타입 설정.                                  |

-   Return

    -   true : 생성 성공.
    -   false : 생성 실패.

-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### restartAnimation(restartRate) → boolean

> 그래프 애니메이션을 다시 실행합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type   | Description                                                                                |
| :---------- | :----- | :----------------------------------------------------------------------------------------- |
| restartRate | number | <p>애니메이션 시작 위치 설정<br>0.0: 애니메이션 시작 위치.<br>1.0: 애니메이션 끝 위치.</p> |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var graph = Module.createBarGraph("Graph");
//...
graph.restartAnimation(0.5);
```

{% endtab %}
{% endtabs %}

### setValueRange(min, max, interval) → boolean

> 그래프 Y축 범위를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description         |
| :------- | :----- | :------------------ |
| min      | number | 그래프 Y축 최소 값. |
| max      | number | 그래프 Y축 최대 값. |
| interval | number | 그래프 격자 간격.   |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setAnimationSpeed(speed) → boolean

> 그래프 애니메이션 실행 속도를 설정합니다.
>
> 입력 변수값(speed)는 0.1 ~ 1.0 사이 값을 가지며 1.0 가까울 수록 빠르게 재생합니다..

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                 |
| :---- | :----- | :-------------------------- |
| speed | number | 그래프 애니메이션 실행 속도 |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFloorColor(color) → boolean

> 그래프 바닥 평면 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| :---- | :---------------------------- | :---------- |
| color | [JSColor](../core/jscolor.md) | 색상.       |

-   Return
    -   true : 설정 설공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setLegendBoxSize(size) → boolean

> 범례 색상 표시 박스 크기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                            | Description |
| :--- | :------------------------------ | :---------- |
| size | [JSSize3D](../core/jssize3d.md) | 박스 크기.  |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setUnitText(text) → boolean

> 그래프 Y축에 해당되는 범례(단위)에 대한 문자열을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| :--- | :----- | :----------- |
| text | string | 단위 문자열. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setGridVisible(type) → boolean

> 그래프 Y축과 격자를 가시화 유무 설정 합니다..

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                            |
| :--- | :------ | :--------------------------------------------------------------------- | --- |
| type | boolean | <p>true인 경우 Y축 격자 가시화(RTT)<br>false인 경우 Y축 격자 숨김.</p> |     |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### insertLegend(name, label, color) → boolean

> 그래프 범례를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description            |
| :---- | :---------------------------- | :--------------------- |
| name  | string                        | 그래프 범례 그룹 명칭. |
| label | string                        | 그래프 범례 명칭.      |
| color | [JSColor](../core/jscolor.md) | 그래프 범례 색상.      |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript
var graph = Module.createBarGraph("Graph");
graph.insertLegend("Legend1", "Gas", new Module.JSColor(200, 255, 0, 0));
graph.insertLegend("Legend2", "Electricity", new Module.JSColor(200, 255, 255, 0));
graph.insertLegend("Legend3", "Water", new Module.JSColor(200, 0, 0, 255));
graph.insertLegend("Legend4", "Others", new Module.JSColor(200, 255, 255, 255));
```

{% endtab %}
{% endtabs %}

### insertDataSet(name, data) → boolean

> 그래프 데이터 셋을 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                                | Description                                                  |
| :--- | :---------------------------------- | :----------------------------------------------------------- |
| name | string                              | 데이터 셋 명칭 (그래프 하단 텍스트 출력).                    |
| data | [Collection](../core/collection.md) | 데이터 값 리스트 (범례 추가 순서를 따르며, 범례와 1:1 대응). |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript
var graph = Module.createBarGraph("Graph");

var dataValue = [10.5, 50.1, 97.0, 11.6, 34.9];
var data = new Module.Collection();

for (var i = 0, len = dataValue.length; i < len; i++) {
    data.add(dataValue[i]);
}

graph.insertDataSet("2010", data);
```

{% endtab %}
{% endtabs %}

### setDataSetNameFont(name, font) → boolean

> 데이터 셋 가시화 문자열에 적용할 폰트를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| :--- | :----- | :-------------- |
| name | string | 데이터 셋 이름. |
| font | string | 폰트 이름.      |

-   Return

    -   true : Font setting successful.
    -   false : Font setting failed.

-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setDataSetNameTextSize(name, size) → boolean

> 데이터 셋 가시화 문자열에 적용할 폰트 크기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| :--- | :----- | :-------------- |
| name | string | 데이터 셋 이름. |
| size | number | 폰트 크기.      |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setDataSetNameTextColor(name, textcolor, textOutlineColor) → boolean

> 데이터 셋 가시화 문자열에 적용할 폰트 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name             | Type                          | Description       |
| :--------------- | :---------------------------- | :---------------- |
| name             | string                        | 데이터 셋 이름.   |
| textcolor        | [JSColor](../core/jscolor.md) | 텍스트 채움 색상. |
| textOutlineColor | [JSColor](../core/jscolor.md) | 텍스트 외곽 색상. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setDataSetNameInterval(value) → boolean

> 그래프 화면과 필드 이름 텍스트 간 간격을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                             |
| :---- | :----- | :-------------------------------------- |
| value | number | 그래프 화면과 필드 이름 텍스트 간 간격. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFloorDepth(value) → boolean

> 그래프 바닥 평면 세로방향 너비를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description |
| :---- | :----- | :---------- |
| value | number | 너비.       |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   the createGraph function 참조.
    -   [Sandbox_2D Bar Graph](https://sandbox.egiscloud.com/code/main.do?id=object_graph_bar_2d_stack)

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
