---
description: 지도 내 지형 설정 및 제어하기 위한 API 입니다.
---

# JSTerrain

> Module.getTerrain() API를 생성합니다.

```javascript
var map = Module.getTerrain();
```

## Properties
|Name|Type|Description|
|------|------|------|
|demRate|number|DEM 높이 표현 비율|
|recoverHSV|number|색상 조정 설정 여부|
|recoverHue|number|색상 Hue 조정 값|
|recoverSaturation|number|색상 Saturation 조정 값|
|recoverValue|number|색상 Value 조정 값|

## Function

### makeTerrainElevationCellData(option) → object

> 입력된 정점 좌표 목록을 기반으로 변수값 격자 구조를 생성하고 정보를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                      | Description |
| ------ | --------------------------------------------------------- | ----------- |
| option | [JSTerrain.GridOption](jsterrain.md#jsterrain.gridoption) | 속성 정보.  |

-   Return
    -   .result: API success status ( 1 : success, 0 : failure ).
    -   .name: Name of the operation API.
    -   .return: API return information ( [JSTerrain.GridData](jsterrain.md#jsterrain.griddata) : Normal return value, string : Failure error code ).

{% endtab %}
{% tab title="Template" %}

```javascript
let point = new Module.JSVec3Array();
point.push(new Module.JSVector3D(127.01969238371277, 37.56514815604788, 24.40620245039463));
point.push(new Module.JSVector3D(127.01962748647728, 37.56392380491751, 25.515124042518437));
point.push(new Module.JSVector3D(127.02194230953037, 37.56375530181643, 33.266184841282666));
point.push(new Module.JSVector3D(127.02220846619382, 37.56494396175599, 26.32035342976451));

let parameter = {
    coordinates: {
        style: "JSVector3D",
        coordinate: point,
    },
    vertical: 10,
    horizontal: 10,
};
let result = Module.getTerrain().makeTerrainElevationCellData(parameter);
```

{% endtab %}
{% endtabs %}

### getServerAltitude(options, callback) → boolean

> 입력된 좌표 목록에 대해 서버로부터 고도값을 요청하고, 결과를 콜백 함수로 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type     | Description                                     |
| -------- | -------- | ----------------------------------------------- |
| options  | object   | 요청할 좌표 정보.                               |
| callback | function | 요청 완료 후 결과 고도값을 반환하는 콜백 함수. |

#### options 구조

| Key       | Type        | Description                                       |
| --------- | ----------- | ------------------------------------------------- |
| level     | number      | 요청할 지형 타일 레벨.                            |
| positions | array       | 고도 요청할 좌표 목록. 2D 배열(lon, lat) 또는 [JSVec2Array](../core/jsvec2array.md) 가능. |

-   Return  
    -   `true`: 요청 성공.  
    -   `false`: 파라미터 오류 또는 실패.

-   Error Conditions
    -   `callback`이 함수가 아닌 경우.
    -   `positions`가 배열도 JSVec2Array도 아닌 경우.
    -   `level` 또는 `positions`가 누락된 경우.

-   Sample
    -   [Sandbox_TerrainAltitude](https://sandbox.egiscloud.com/code/main.do?id=terrain_dem_from_server)

{% endtab %}
{% tab title="Template" %}

```javascript
var input = {
    level: 10,
    positions: [
        [127.01, 37.55],
        [127.02, 37.56]
    ]
};

Module.getTerrain().getServerAltitude(input, function (result) {
    console.log("Altitude result:", result);
});
```

{% endtab %}
{% endtabs %}


### setImageMask(option) → bool

> 지정한 경위도 사각 범위 바깥의 지역을 임의의 색상으로 마스킹합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                              | Description |
| ------ | ----------------------------------------------------------------- | ----------- |
| option | [JSTerrain.MaskingOptions](jsterrain.md#jsterrain.maskingoptions) | 속성 정보    |

-   Return
    -   성공 시 true, 실패 시 false를 반환합니다.

-   Sample
    -   [Sandbox_RequestBoundary](https://sandbox.egiscloud.com/code/main.do?id=layer_building_request_boundary)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getTerrain().setImageMask({
    active : true,
    range : {
        min : [126.930052, 37.529214],
        max : [126.941028, 37.520294]
    },
    color : {
        a : 200,
        r : 0,
        g : 0,
        b : 0
    }
});
```

{% endtab %}
{% endtabs %}



### Type Definitions

#### JSTerrain.GridOption

> Basic Grid setting options.

| Name       | Type                                                    | Attributes | Default | Description                                                                                     |
| ---------- | ------------------------------------------------------- | ---------- | ------- | ----------------------------------------------------------------------------------------------- |
| option     | [coordinates Type](../etc/tag-list.md#coordinates-type) |            |         | List of latitude and longitude coordinates for the analysis area, coordinate list type setting. |
| vertical   | number                                                  | optional   | 5       | Length of the Cell composing the Grid vertically (in meters).                                   |
| horizontal | number                                                  | optional   | 5       | Length of the Cell composing the Grid horizontally (in meters).                                 |

#### JSTerrain.GridData

> Grid return information.

| Name            | Type                                                  | Description                                                     |
| --------------- | ----------------------------------------------------- | --------------------------------------------------------------- |
| min             | [JSVector2D](../core/jsvector2d.md)                   | Lower left latitude and longitude coordinates of the Grid.      |
| max             | [JSVector2D](../core/jsvector2d.md)                   | Upper right latitude and longitude coordinates of the Grid.     |
| center          | [JSVector2D](../core/jsvector2d.md)                   | Center latitude and longitude coordinates of the Grid.          |
| vertical        | number                                                | Length of the Cell composing the Grid vertically (in meters).   |
| verticalCount   | number                                                | Number of Cells composing the Grid vertically.                  |
| horizontal      | number                                                | Length of the Cell composing the Grid horizontally (in meters). |
| horizontalCount | number                                                | Number of Cells composing the Grid horizontally.                |
| cells           | [JSTerrain.CellData](jsterrain.md#jsterrain.celldata) | Array of Cell information composing the Grid.                   |

#### JSTerrain.CellData

> Data information of the Cell composing the Grid.

| Name      | Type                                | Description                                                      |
| --------- | ----------------------------------- | ---------------------------------------------------------------- |
| type      | boolean                             | Inclusion status of the analysis area.                           |
| elevation | number                              | Elevation of the cell center latitude and longitude coordinates. |
| min       | [JSVector2D](../core/jsvector2d.md) | Lower left latitude and longitude coordinates of the Cell.       |
| max       | [JSVector2D](../core/jsvector2d.md) | Upper right latitude and longitude coordinates of the Cell.      |
| center    | [JSVector2D](../core/jsvector2d.md) | Center latitude and longitude coordinates of the Cell.           |

#### JSTerrain.MaskingOptions

> 지형 영상 마스킹 옵션 속성

| Name      | Type     | Description                                           |
| --------- | -------- | ------------------------------------------------------|
| active    | boolean  | 옵션 활성화 여부                                         |
| range     | object   | 2차원 경위도 좌표 min, max 속성으로 이루어진 마스킹 범위     |
| color     | object   | 0~255 사이 정수 a, r, g, b 속성으로 이루어진 마스킹 색상 값 |
