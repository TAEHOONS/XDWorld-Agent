---
description: 지도 내 3차원 격자 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSColorGrid3D

Module.createColorGrid3D() API를 생성합니다.

```javascript
var colorGrid3D = Module.createColorGrid3D("ID");
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

### SetGridPosition(leftTop, rightTop, rightBottom, leftBottom, altitude, row, col) → number

> 3차원 격자의 각 꼭지점 좌표(경도, 위도)를 기준으로 격자 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                | Description             |
| ----------- | ----------------------------------- | ----------------------- |
| leftTop     | [JSVector2D](../core/jsvector2d.md) | 좌상단 좌표(경도 위도). |
| rightTop    | [JSVector2D](../core/jsvector2d.md) | 우상단 좌표(경도 위도). |
| rightBottom | [JSVector2D](../core/jsvector2d.md) | 우하단 좌표(경도 위도). |
| leftBottom  | [JSVector2D](../core/jsvector2d.md) | 좌하단 좌표(경도 위도). |
| altitude    | number                              | 객체 높이.              |
| row         | number                              | 그리드 가로 개수.       |
| col         | number                              | 그리드 세로 개수.       |

-   Return

    -   number: 격자를 구성하는 cell 갯수.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
var gridCellNum = colorGrid3D.SetGridPosition(new Module.JSVector2D(124.2, 39), new Module.JSVector2D(130.5, 39), new Module.JSVector2D(130.5, 34.5), new Module.JSVector2D(124.2, 34.5), 1000.0, 100, 100);
```

{% endtab %}
{% endtabs %}

### SetGridCellDefaultColor(color) → boolean

> 3차원 격자 객체에 표현될 색상값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description  |
| ----- | ----------------------------- | ------------ |
| color | [JSColor](../core/jscolor.md) | 격자 생상값. |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetGridCellDefaultColor(new Module.JSColor(255, 255, 255, 0));
```

{% endtab %}
{% endtabs %}

### SetGridCellColor(row, column, color) → boolean

> 입력 변수값(row, colum)으로 해당되는 cell을 색상값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                          | Description       |
| ------ | ----------------------------- | ----------------- |
| row    | number                        | 가로 인덱스 번호. |
| column | number                        | 세로 인덱스 번호. |
| color  | [JSColor](../core/jscolor.md) | Cell 색상값.      |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   입력 변수값(row, column)이 3차원 격자 보다 큰값이 들어온 경우.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetGridCellColor(0, 0, new Module.JSColor(255, 255, 0, 0));
```

{% endtab %}
{% endtabs %}

### SetGridLineColor(color) → boolean

> 3차원 격자 객체의 테두리 색상값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| color | [JSColor](../core/jscolor.md) | 색상값.     |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   3차원 격자 객체의 테두리 생성 옵션을 설정하지 않은 경우.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetGridLineColor(new Module.JSColor(150, 255, 0, 0));
```

{% endtab %}
{% endtabs %}

### SetGridCellLineColor(row, column, color) → boolean

> 입력 변수값(row, colum)으로 해당되는 cell을 테두리 색상값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                          | Description         |
| ------ | ----------------------------- | ------------------- |
| row    | number                        | 가로 인덱스 번호.   |
| column | number                        | 세로 인덱스 번호.   |
| color  | [JSColor](../core/jscolor.md) | Cell 테두리 색상값. |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건.
        -   입력 변수값(row, column)이 3차원 격자 보다 큰값이 들어온 경우.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetGridCellLineColor(0, 0, new Module.JSColor(150, 255, 0, 0));
```

{% endtab %}
{% endtabs %}

### SetGridCellHeight(row, column, color) → boolean

> 입력 변수값(row, colum)으로 해당되는 cell을 높이값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description              |
| ------ | ------ | ------------------------ |
| row    | number | 가로 인덱스 번호.        |
| column | number | 세로 인덱스 번호.        |
| height | number | cell 높이값(meter 단위). |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   입력 변수값(row, column)이 3차원 격자 보다 큰값이 들어온 경우.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetGridCellHeight(0, 0, 30);
```

{% endtab %}
{% endtabs %}

### SetDrawLine(type) → boolean

> 3차원 격자 객체의 테두리 생성 유무를 설정합니다.
>
> 테두리 생성 유무 초기 설정은 false 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                        |
| ---- | ------- | -------------------------------------------------- |
| type | boolean | <p>true: 테두리 생성.<br>false: 테두리 미생성.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetDrawLine(true);
```

{% endtab %}
{% endtabs %}

### SetNormal(type) → boolean

> 3차원 격자 객체의 음영 효과를 설정합니다.
>
> 음영 효과의 초기 설정은 false 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                              |
| ---- | ------- | -------------------------------------------------------- |
| type | boolean | <p>true: 음영 효과 설정.<br>false: 음영 효과 미설정.</p> |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.SetNormal(true);
```

{% endtab %}
{% endtabs %}

### Create() → boolean

> 설정된 정보를 기준으로 3차원 격자 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

-   Return

    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건.
        -   입력된 좌표 정보가 없는 경우.
        -   설정된 가로, 세로 index 범위를 초과한 경우.

-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_3d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("COLOR_GRID_3D");
colorGrid3D.Create();
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

### getCellWidthCount() → number

> 3차원 격자 객체의 가로(Cell Width) 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return  
    -   number: 가로 방향 셀 개수.  
    -   0: 객체가 없거나 실패한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("GRID_ID");
var widthCount = colorGrid3D.getCellWidthCount();
```

{% endtab %}
{% endtabs %}

### getCellHeightCount() → number

> 3차원 격자 객체의 세로(Cell Height) 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return  
    -   number: 세로 방향 셀 개수.  
    -   0: 객체가 없거나 실패한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("GRID_ID");
var heightCount = colorGrid3D.getCellHeightCount();
```

{% endtab %}
{% endtabs %}

### getCellColor(row, column) → [JSColor](../core/jscolor.md)

> 지정한 셀(row, column)의 색상값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| row    | number | 가로 인덱스 번호. |
| column | number | 세로 인덱스 번호. |

-   Return  
    -   [JSColor](../core/jscolor.md): 셀의 색상값.  
    -   실패 시 기본 색상 반환.

-   실패 조건  
    -   row 또는 column이 유효하지 않을 경우.  
    -   내부 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid3D = Module.createColorGrid3D("GRID_ID");
var cellColor = colorGrid3D.getCellColor(0, 0);
```

{% endtab %}
{% endtabs %}
