---
description: 지도 내 2차원 격자 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSColorGrid

> Module.createColorGrid() API를 생성합니다.

```javascript
var colorGrid = Module.createColorGrid("ID");
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

> 2차원 격자의 각 꼭지점 좌표(경도, 위도)를 기준으로 격자 객체를 생성합니다.

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
    -   [Sandbox_Grid(2D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_2d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid("COLOR_GRID_2D");
var gridCellNum = colorGrid2D.SetGridPosition(new Module.JSVector2D(124.2, 39), new Module.JSVector2D(130.5, 39), new Module.JSVector2D(130.5, 34.5), new Module.JSVector2D(124.2, 34.5), 100000.0, 100, 100);
```

{% endtab %}
{% endtabs %}

### SetGridPositionByCellOptions(leftTop, altitude, width, height, row, col) → number

> 격자의 좌상단 기준 좌표(경도, 위도)를 기준으로 2차원 격자 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description             |
| -------- | ----------------------------------- | ----------------------- |
| leftTop  | [JSVector2D](../core/jsvector2d.md) | 좌상단 좌표(경도 위도). |
| altitude | number                              | 객체 높이.              |
| width    | number                              | 그리드 가로 길이.       |
| height   | number                              | 그리드 세로 길이.       |
| row      | number                              | 그리드 가로 개수.       |
| col      | number                              | 그리드 세로 개수.       |

-   Return
    -   number: 격자를 구성하는 cell 갯수.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid("COLOR_GRID_2D");
var gridCellNum = colorGrid2D.SetGridPositionByCellOptions(new Module.JSVector2D(124.2, 39), 100000.0, 1000, 1000, 100, 100);
```

{% endtab %}
{% endtabs %}

### SetGridPositionByCellSize(leftTop, rightBottom, altitude, width, height) → number

> 최소, 최대 위치 좌표(경도 위도)를 기준으로 2차원 격자 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                | Description             |
| ----------- | ----------------------------------- | ----------------------- |
| leftTop     | [JSVector2D](../core/jsvector2d.md) | 좌상단 좌표(경도 위도). |
| rightBottom | [JSVector2D](../core/jsvector2d.md) | 우하단 좌표(경도 위도). |
| altitude    | number                              | 객체 높이.              |
| width       | number                              | 그리드 가로 길이.       |
| height      | number                              | 그리드 세로 길이.       |

-   Return
    -   number: 격자를 구성하는 cell 갯수.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid("COLOR_GRID_2D");
var gridCellNum = colorGrid2D.SetGridPositionByCellSize(new Module.JSVector2D(124.2, 39), new Module.JSVector2D(130.5, 34.5), 100000.0, 1000, 1000);
```

{% endtab %}
{% endtabs %}

### SetGridCellDefaultColor(color) → boolean

> 2차원 격자 객체에 표현될 색상값을 설정합니다.

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
    -   [Sandbox_Grid(2D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_2d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetGridCellDefaultColor(new Module.JSColor(255, 255, 255, 0));
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
        -   입력 변수값(row, column)이 2차원 격자 보다 큰값이 들어온 경우.
-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(2D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_2d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetGridCellColor(0, 0, new Module.JSColor(255, 255, 0, 0));
```

{% endtab %}
{% endtabs %}

### SetLeftToRightSlopeAngle(angle) → boolean

> X축 기울기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description           |
| ----- | ------ | --------------------- |
| angle | number | 기울기(degrees 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetLeftToRightSlopeAngle(30);
```

{% endtab %}
{% endtabs %}

### SetLeftToRightSlopeAngleByAltitude(left, right) → boolean

> 왼쪽, 오른쪽 고도값 기준 기울기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description       |
| ----- | ------ | ----------------- |
| left  | number | 왼쪽 기준 고도.   |
| right | number | 오른쪽 기준 고도. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetLeftToRightSlopeAngleByAltitude(100000, 150000);
```

{% endtab %}
{% endtabs %}

### SetFrontToBackSlopeAngle(angle) → boolean

> Y축 기울기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description           |
| ----- | ------ | --------------------- |
| angle | number | 기울기(degrees 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetFrontToBackSlopeAngle(30);
```

{% endtab %}
{% endtabs %}

### SetFrontToBackSlopeAngleByAltitude(top, bottom) → boolean

> 위, 아래 고도값 기준 기울기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description       |
| ----- | ------ | ----------------- |
| left  | number | 위쪽 기준 고도.   |
| right | number | 아래쪽 기준 고도. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패..

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetFrontToBackSlopeAngleByAltitude(100000, 150000);
```

{% endtab %}
{% endtabs %}

### SetDirectionAngle(angle) → boolean

> 2차원 격자 객체의 방향을 설정합니다.
>
> 입력 변수값(angle)에 따른 회전 정보
>
> -   0, 360: 부쪽.
> -   90: 동쪽.
> -   180: 남쪽.
> -   270: 서쪽.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description         |
| ----- | ------ | ------------------- |
| angle | number | 뱡향(degrees 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetDirectionAngle(0);
```

{% endtab %}
{% endtabs %}

### SetTerrainUnion(union) → boolean

> 2차원 격자 객체와 지형 결합 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    | Description                                       |
| ----- | ------- | ------------------------------------------------- |
| union | boolean | <p>true: 지형결합.<br>false: 객체 위치 기준.</p>. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetTerrainUnion(true);
```

{% endtab %}
{% endtabs %}

### SetTerrainUnionGap(altitude) → boolean

> 2차원 격자 객체와 지형 결합 후 높이값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description         |
| -------- | ------ | ------------------- |
| altitude | number | 지형으로 부터 높이. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetTerrainUnion(true);
colorGrid2D.SetTerrainUnionGap(100);
```

{% endtab %}
{% endtabs %}

### SetDrawLine(type) → boolean

> 2차원 격자 객체의 테두리 생성 유무를 설정합니다.
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
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetDrawLine(true);
```

{% endtab %}
{% endtabs %}

### SetGridLineColor(color) → boolean

> 2차원 격자 객체의 테두리 색상값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| color | [JSColor](../core/jscolor.md) | 색상값.     |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   2차원 격자 객체의 테두리 생성 옵션을 설정하지 않은 경우.
-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(2D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_2d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.SetGridLineColor(new Module.JSColor(255, 255, 0, 0));
```

{% endtab %}
{% endtabs %}

### GetGridLeftTopPosition() → [JSVector3D](../core/jsvector3d.md)

> 2차원 격자 객체의 좌상단 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 좌상단 좌표(경도, 위도, 고도) 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var position = colorGrid2D.GetGridLeftTopPosition();
var lon = position.Longitude;
var lat = position.Latitude;
var alt = position.Altitude;
```

{% endtab %}
{% endtabs %}

### GetGridRightTopPosition() → [JSVector3D](../core/jsvector3d.md)

> 2차원 격자 객체의 우상단 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 우상단 좌표(경도, 위도, 고도) 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var position = colorGrid2D.GetGridRightTopPosition();
var lon = position.Longitude;
var lat = position.Latitude;
var alt = position.Altitude;
```

{% endtab %}
{% endtabs %}

### GetGridLeftBottomPosition() → [JSVector3D](../core/jsvector3d.md)

> 2차원 격자 객체의 좌하단 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 좌하단 좌표(경도, 위도, 고도) 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
//...set grid object options...
colorGrid2D.Create();

var position = colorGrid2D.GetGridLeftBottomPosition();

var lon = position.Longitude;
var lat = position.Latitude;
var alt = position.Altitude;
```

{% endtab %}
{% endtabs %}

### GetGridRightBottomPosition() → [JSVector3D](../core/jsvector3d.md)

> 2차원 격자 객체의 우하단 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 우하단 좌표(경도, 위도, 고도) 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var position = colorGrid2D.GetGridRightBottomPosition();
var lon = position.Longitude;
var lat = position.Latitude;
var alt = position.Altitude;
```

{% endtab %}
{% endtabs %}

### GetGridCellPosition(row, column) → [JSVector3D](../core/jsvector3d.md)

> 입력 변수값(row, colum)으로 해당되는 cell을 중심 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| row    | number | 가로 인덱스 번호. |
| column | number | 세로 인덱스 번호. |

-   Return
    -   [JSVector3D](../core/jsvector3d.md): cell 중심 좌표(경도, 위도, 고도) 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var position = colorGrid2D.GetGridCellPosition(0, 0);
var lon = position.Longitude;
var lat = position.Latitude;
var alt = position.Altitude;
```

{% endtab %}
{% endtabs %}

### GetGridCellRect(row, column) → [JSVec3Array](../core/jsvec3array.md)

> 입력 변수값(row, colum)으로 해당되는 cell을 꼭지점 좌표(경도, 위도, 고도) 목록 정보를 반환합니다.
>
> 반환 꼭지점 좌표(경도, 위도, 고도) 정보
>
> -   좌상단 좌표, 우상단 좌표, 좌하단 좌표, 우하단 좌표

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| row    | number | 가로 인덱스 번호. |
| column | number | 세로 인덱스 번호. |

-   Return
    -   [JSVec3Array](../core/jsvec3array.md): cell 꼭지점 좌표 목록 반환 성공
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var position = colorGrid2D.GetGridCellRect(0, 0);

var leftTop = position.get(0);
var rightTop = position.get(1);
var rightbottom = position.get(2);
var leftbottom = position.get(3);

var lon = leftTop.Longitude;
var lat = leftTop.Latitude;
var alt = leftTop.Altitude;
```

{% endtab %}
{% endtabs %}

### GetGridCellIndexByPosition(position) → string

> 입력 변수값(position)에 해당되는 2차원 격자 객체를 구성하는 cell 인덱스 정보를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                  |
| -------- | ----------------------------------- | ---------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 지점 좌표(경도, 위도, 고도). |

-   Return
    -   string: cell 인덱스 정보 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var Index = colorGrid2D.GetGridCellIndexByPosition(new Module.JSVector2D(124.2, 39.5, 100));
```

{% endtab %}
{% endtabs %}

### GetGridEdgeLinePosition(type, value) → [JSVec3Array](../core/jsvec3array.md)

> 2차원 격자 객체 테두리 시작, 끝 점에 해당하는 좌표를 반환합니다.
>
> 입력 변수값(type)에 따른 좌표 반환 정보.
>
> -   0: top.
> -   1: right.
> -   2: bottom.
> -   3: left.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description       |
| ----- | ------ | ----------------- |
| type  | string | 반환 정보 설정값. |
| value | number | 테두리 margin.    |

-   Return
    -   [JSVec3Array](../core/jsvec3array.md): 테두리 시작, 끝 지점에 대한 좌표(경도, 위도, 고도) 반환 성공.
    -   null: 반환 실패.
    -   실패 조건
        -   입력 변수값(type)이 지정된 값이 아닌 값이 입력된 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();

var linelist = colorGrid2D.GetGridEdgeLinePosition(0, 0);
```

{% endtab %}
{% endtabs %}

### Create() → boolean

> 설정된 정보를 기준으로 2차원 격자 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   입력된 좌표 정보가 없는 경우.
        -   설정된 가로, 세로 index 범위를 초과한 경우.
-   Sample
    -   function showGrid 참조.
    -   [Sandbox_Grid(2D)](https://sandbox.egiscloud.com/code/main.do?id=object_grid_2d)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorGrid2D = Module.createColorGrid2D("COLOR_GRID_2D");
colorGrid2D.Create();
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

### createHexagonGrid(options) → boolean

> 지정된 영역에 육각형 셀 그리드를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description             |
| ------- | ------ | ----------------------- |
| options | object | 육각형 그리드 설정 정보 |

#### options 구조

| Key              | Type                                  | Required | Default        | Description                                                                 |
|------------------|---------------------------------------|----------|----------------|-----------------------------------------------------------------------------|
| area             | [JSVec2Array](../core/jsvec2array.md) | true     | -              | 경위도 기준의 영역 좌표 리스트.                                            |
| cellSize         | number                                | true     | -              | 셀의 한 변 길이 (단위: meter).                                             |
| altitude         | number                                | false    | 0.0            | 셀의 고도.                                                                 |
| defaultCellColor | [JSColor](../core/jscolor.md)         | false    | (255,255,255)  | 색상이 지정되지 않은 셀의 기본 색상.                                      |
| cellColorList    | array<object>                         | false    | []             | 위치별 셀 색상 설정 리스트.                                               |

#### cellColorList 항목 구조

| Key       | Type                         | Description               |
|-----------|------------------------------|---------------------------|
| longitude | number                       | 색상을 적용할 셀의 경도.  |
| latitude  | number                       | 색상을 적용할 셀의 위도.  |
| color     | [JSColor](../core/jscolor.md) | 적용할 색상 값.            |

- **Return**  
  - `true`: 생성 성공  
  - `false`: 파라미터 오류 또는 생성 실패

{% endtab %}
{% tab title="Template" %}

```javascript
var area = new Module.JSVec2Array();
area.push(new Module.JSVector2D(126.9, 37.5));
area.push(new Module.JSVector2D(126.91, 37.5));
area.push(new Module.JSVector2D(126.91, 37.51));
area.push(new Module.JSVector2D(126.9, 37.51));

var cellColorList = [
  { longitude: 126.905, latitude: 37.505, color: new Module.JSColor(255, 0, 0) },
  { longitude: 126.906, latitude: 37.506, color: new Module.JSColor(0, 255, 0) }
];

var options = {
  area: area,
  cellSize: 50,
  altitude: 10,
  defaultCellColor: new Module.JSColor(200, 200, 200),
  cellColorList: cellColorList
};

var grid = Module.createColorGrid("GRID_ID");
grid.createHexagonGrid(options);
```

{% endtab %}
{% endtabs %}
