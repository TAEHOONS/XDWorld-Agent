---
description: 수학적 알고리즘 처리를 위한 API 입니다.
---

# JSMath

> Module.getMath() API를 생성합니다.

```javascript
var math = Module.getMath();
```

### convertBezierCurve(options) → [JSVec3Array](../core/JSVec3Array.md)

> 경위도 좌표 목록 정보를 통해 베지어 곡선이 적용된 좌표 목록 반환합니다..
>
> argument 변수로 좌표 변환 옵션을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                               | Description |
| ------ | -------------------------------------------------- | ----------- |
| option | [JSMath.BezierCurve](jsmath.md#jsmath.beziercurve) | 속성 정보.  |

-   Return
    -   [JSVec3Array](../core/JSVec3Array.md): 변환 성공
    -   size 0: 변환 실패.
-   Sample
    -   function createCurvedLine 참조.
    -   [Sandbox_LineInterpolation(Curved)](https://sandbox.egiscloud.com/code/main.do?id=object_line_interpolate_curved)

{% endtab %}
{% tab title="Template" %}

```javascript
var vertices = [];

vertices.push([lon, lat, alt]);
vertices.push([lon, lat, alt]);
vertices.push([lon, lat, alt]);

let curve_pos = {
    coordinate: vertices,
    style: "XYZ",
};
```

{% endtab %}
{% endtabs %}

### convertBeZierLine(options) → object

> 시작, 끝 경위도 좌표도 기준으로 베지어 곡선 좌표 목록을 반환합니다.
>
> argument 변수로 좌표 변환 옵션을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                             | Description |
| ------ | ------------------------------------------------ | ----------- |
| option | [JSMath.BezierLine](jsmath.md#jsmath.bezierline) | 속성 정보.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( object : 정상적인 반환값, 문자열 : 실패 에러 코드 ).
-   Sample
    -   function createBallPath 참조
    -   [Sandbox_ParabolicLine](https://sandbox.egiscloud.com/code/main.do?id=object_line_arc)

{% endtab %}
{% tab title="Template" %}

```javascript
let parameters = {
    start: new Module.JSVector3D(127.94080035885989, 36.336424549396064, 306.52637346833944),
    end: new Module.JSVector3D(127.9419239501012, 36.33615414434727, 300.5711971661076),
    detail: 100,
    height: 330,
    percent: 70,
};
```

{% endtab %}
{% endtabs %}

### calculationSlopeAnalysis(options) → object

> 3\*3(0 배열 좌상단 9 배열 우하단) 배열값을 통한 경사 분석 결과 반환.
>
> argument 변수로 좌표 변환 옵션을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                               | Description |
| ------ | -------------------------------------------------- | ----------- |
| option | [JSMath.SlopeOption](jsmath.md#jsmath.slopeoption) | 속성 정보.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( object : 정상적인 반환값, 문자열 : 실패 에러 코드 ).

{% endtab %}
{% tab title="Template" %}

```javascript
let slop = {
    type: "TERRAIN_DIRECTION_ANGLE",
    array: [101, 92, 85, 101, 92, 85, 101, 91, 84],
    vertical: 10,
    horizontal: 10,
};
let result = Module.getMath().calculationSlopeAnalysis(slop);
```

{% endtab %}
{% endtabs %}

### splitLine(options) → object

> 경위도 좌표 목록을 일정 간격으로 분할한 결과를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                             |
| ------- | ------- | ------------------------------------------------------- |
| options | object  | `coordinates` 정보와 `split` 수치를 포함한 옵션 객체. |

-   options 구조

| Key         | Type      | Description                                          |
| ----------- | --------- | ---------------------------------------------------- |
| coordinates | object    | 좌표 정보 `{ style, coordinate }`.                 |
| split       | number    | 나눌 정점 개수. 기본값: 100                         |

-   Return  
    -   `.result`: API 성공 여부 (1: 성공, 0: 실패)  
    -   `.name`: API 명칭  
    -   `.return`: `{ length, count, data }` 객체 반환  
        - `length`: 전체 거리 (meter)  
        - `count`: 좌표 개수  
        - `data`: [JSVec3Array](../core/JSVec3Array.md) 형태의 분할 좌표

{% endtab %}
{% tab title="Template" %}

```javascript
let coordinates = {
    style: "XYZ",
    coordinate: [
        [127.0, 37.5, 10],
        [127.001, 37.501, 10]
    ]
};

let option = {
    coordinates: coordinates,
    split: 10
};

let result = Module.getMath().splitLine(option);
```

{% endtab %}
{% endtabs %}


### Type Definitions

#### JSMath.BezierCurve

> 경위도 좌표 목록 정보를 베지어 곡선 변환 옵션.

| Name   | Type                                                 | Attributes | Default | Description                            |
| ------ | ---------------------------------------------------- | ---------- | ------- | -------------------------------------- |
| option | [coordinates Type](tag-list.md#coordinate-type-list) |            |         | 경위도 좌표 목록, 좌표 목록 타입 설정. |

#### JSMath.BezierLine

> 경위도 좌표 목록 정보를 포물선 곡선 변환 옵션.

| Name    | Type                                | Attributes | Default | Description                                                   |
| ------- | ----------------------------------- | ---------- | ------- | ------------------------------------------------------------- |
| start   | [JSVector3D](../core/jsvector3d.md) |            | 500     | 직선 경위도 시작 위치.                                        |
| end     | [JSVector3D](../core/jsvector3d.md) |            | 10      | 직선 경위도 끝 위치.                                          |
| detail  | number                              | optional   | 50      | 곡선 생성 보간 점 수.                                         |
| height  | number                              | optional   | 100     | 곡선 최대 높이.                                               |
| percent | number                              | optional   | 50      | 시작 위치 0%, 끝 위치 100% 기준으로 곡선 최대 높이 지점 설정. |

### getIntervalPositionInRect(min, max, vertical, horizontal) → object

> 경위도 기준의 사각 영역 내에서 일정 간격마다 좌표를 균등 분포로 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type                                | Description                                   |
| ---------- | ----------------------------------- | --------------------------------------------- |
| min        | [JSVector2D](../core/jsvector2d.md) | 사각 영역의 최소 좌표 (경도, 위도).             |
| max        | [JSVector2D](../core/jsvector2d.md) | 사각 영역의 최대 좌표 (경도, 위도).             |
| vertical   | number                              | 세로 간격 (meter 단위).                         |
| horizontal | number                              | 가로 간격 (meter 단위).                         |

-   Return  
    -   `position`: [JSVec2Array](../core/jsvec2array.md) 타입의 좌표 목록  
    -   `positionCountWidth`: 가로 개수  
    -   `positionCountHeight`: 세로 개수  

{% endtab %}
{% tab title="Template" %}

```javascript
let min = new Module.JSVector2D(127.0, 37.5);
let max = new Module.JSVector2D(127.01, 37.51);

let result = Module.getMath().getIntervalPositionInRect(min, max, 10, 10);
```

{% endtab %}
{% endtabs %}

### isPointInPolygon(polygon, points) → Array<boolean>

> 주어진 2D 포인트들이 폴리곤 내부에 포함되는지를 판별합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                             | Description                                         |
| ------- | -------------------------------- | -------------------------------------------------- |
| polygon | [JSVec2Array](../core/jsvec2array.md) | 다각형 영역 경계 좌표 목록.                         |
| points  | Array<[number, number]>          | 경위도 좌표 쌍(경도, 위도) 목록.                   |

-   Return  
    -   `Array<boolean>`: 각 포인트가 폴리곤 안에 포함되는 여부를 `true` 또는 `false`로 반환하는 배열.

{% endtab %}
{% tab title="Template" %}

```javascript
let polygon = new Module.JSVec2Array();
polygon.push(new Module.JSVector2D(127.0, 37.5));
polygon.push(new Module.JSVector2D(127.01, 37.5));
polygon.push(new Module.JSVector2D(127.01, 37.51));
polygon.push(new Module.JSVector2D(127.0, 37.51));

let points = [
    [127.005, 37.505],   // 내부
    [127.02, 37.52]      // 외부
];

let result = Module.getMath().isPointInPolygon(polygon, points);
// result => [true, false]
```

{% endtab %}
{% endtabs %}

### getClosestPositionOnPath(point, path) → object

> 한 점에서부터 path 까지의 거리 중 가장 가까운 위치의 정보를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                  | Description |
| ----- | ------------------------------------- | ----------- |
| point | [JSVector3D](../core/jsvector3d.md)   | 기준 점      |
| path  | [JSVec3Array](../core/jsvec3array.md) | path array  |

-   Description
    - 가장 가까운 점이 선분 범위 밖에 위치하는 경우 path의 시작점 또는 끝점을 반환합니다.
    - 가장 가까운 점이 선분 내에 위치하는 경우 해당 지점의 좌표 정보를 반환합니다.
-   Return
    -   object
        -   distance : 거리
        -   position : 좌표
        -   index : path 인덱스

{% endtab %}
{% tab title="Template" %}

```javascript
let point = new Module.JSVector3D(127.003, 37.49, 10);
let path = new Module.JSVec3Array();
path.push(new Module.JSVector2D(127.0, 37.5));
path.push(new Module.JSVector2D(127.01, 37.5));
path.push(new Module.JSVector2D(127.01, 37.51));
path.push(new Module.JSVector2D(127.0, 37.51));

let closestPosition = Module.getMath().getClosestPositionOnPath(point, path);
// closestPosition.distance
// closestPosition.position
// closestPosition.index
```

{% endtab %}
{% endtabs %}

### getScreenEdgeIndicator(position) → object \| null

> 화면 밖에 있는 객체의 위치를 화면 경계 기준으로 보정하여 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                                 |
| -------- | ----------------------------------- | ------------------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 대상 객체의 지형 상 위치(경도, 위도, 고도). |

-   Return  
    -   `object`: `{ x, y }` 화면 경계상의 좌표 (픽셀 단위).  
    -   `null`: 객체가 화면 내에 이미 포함되어 있는 경우.

-   Sample  
    -   function getOutOfScreenIndicator 참조  
    -   [Sandbox_Object Indicator](https://sandbox.egiscloud.com/code/main.do?id=coordinate_indicator)

{% endtab %}
{% tab title="Template" %}

```javascript
let position = new Module.JSVector3D(127.01, 37.51, 300.0);
let screenEdge = Module.getMath().getScreenEdgeIndicator(position);

if (screenEdge !== null) {
    console.log("Out of view. Indicator at:", screenEdge.x, screenEdge.y);
}
```

{% endtab %}
{% endtabs %}


#### JSMath.SlopeOption

> 경사 분석 설정 옵션.

| Name       | Type   | Attributes | Default | Description                                                               |
| ---------- | ------ | ---------- | ------- | ------------------------------------------------------------------------- |
| type       | string |            |         | 경사분석 옵션(TERRAIN_ANGLE, TERRAIN_DIRECTION, TERRAIN_DIRECTION_ANGLE). |
| array      | array  |            |         | 경사분석을 위한 [3*3] 해발고도 배열.                                      |
| vertical   | number | optional   | 5       | 경사도 분석에 필요한 Cell 세로 길이(단위 : m).                            |
| horizontal | number | optional   | 5       | 경사도 분석에 필요한 Cell 세로 길이(단위 : m).                            |
