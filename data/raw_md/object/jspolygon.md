---
description: 지도 내 평면 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSPolygon

> Module.createPolygon() API를 생성합니다.

```javascript
var object = Module.createPolygon("ID");
```

## Function

### getArea() → number

> 평면 객체의 면적을 반환합니다.
>
> 평면 객체의 면적은 지형 곡면률을 고려하지 않는 단순 면적값을 계산합니다.
>
> RTT 가시화 중인 평면 객체의 면적과 3D 가시화 평면 객체의 면적은 서로 상이 할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number > 0: 반환 성공.
    -   number == 0: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var area = object.getArea();
```

{% endtab %}
{% endtabs %}

### getBoundary() → [JSAABBox3D](../core/jsaabbox3d.md)

> 평면 객체의 공간 영역 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSAABBox3D](../core/jsaabbox3d.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var boundary = object.getBoundary();
var boundary_min = boundary.min;
var boundary_max = boundary.max;
```

{% endtab %}
{% endtabs %}

### getCenter() → [JSVector3D](../core/jsvector3d.md)

> 객체의 중심 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var vCenter = object.getCenter();
var dCenterLon = vCenter.Longitude;
var dCenterLat = vCenter.Latitude;
var dCenterAlt = vCenter.Altitude;
```

{% endtab %}
{% endtabs %}

### getParts() → [Collection](../core/collection.md)

> 객체의 파트 리스트를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [Collection](../core/collection.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getExtent() → number

> 평면 객체의 공간 영역의 장축 거리를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 거리 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var bExtends = object.getExtent();
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

### loadFile(option) → boolean

> 3ds 포맷 파일 정보를 기반으로 평면 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                              | Description |
| ------ | ----------------------------------------------------------------- | ----------- |
| option | [JSPolygon.loadFileOption](jspolygon.md#jspolygon.loadfileoption) | 속성 정보.  |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   positionmode=true 일 때 projectioncode가 설정되지 않은 경우
        -   positionmode=false 일 때 position이 지정되지 않은 경우
-   Sample
    -   the load3DS function 참조.
    -   [Sandbox_3DS](https://sandbox.egiscloud.com/code/main.do?id=object_file_3ds)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### loadTexture(id, url) → boolean

> 평면 객체에 사용할 이미지를 설정합니다.
>
> 입력 변수값(id)은 [setFaceTexture](jspolygon.md#setfacetexture-index-name-boolean) API로 텍스쳐를 적용할 때 텍스쳐를 구분하는 용도로 사용합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| id   | string | 고유 명칭.  |
| url  | string | 이미지 url. |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   If there is already a texture with the same name.
        -   If name, url are empty strings.
-   Sample
    -   the init function 참조.
    -   [Sandbox_Polygon RTT](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_rtt_image_changing)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setCircle(position, radius, segment)

> 중심 좌표(경도, 위도, 고도)를 기준으로 원 객체를 생성합니다.
>
> 입력 변수값(radius)으로 크기를 설정합니다.
>
> 입력 변수값(radius)은 0보다 큰값, 입력 변수값(segment)은 3보다 큰값이 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                   |
| -------- | ----------------------------------- | ----------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 중심 좌표 (경도, 위도, 고도). |
| radius   | number                              | 반지름 (in meter).            |
| segment  | number                              | 단면의 다각수.                |

-   Sample
    -   the createCirclePolygon function 참조.
    -   [Sandbox_Circle Polygon](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_circle)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setSphere(parameter)

> 중심 좌표(경도, 위도, 고도)를 기준으로 구 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type  | Description                   |
| -------- | ----- | ----------------------------- |
| paramter | Array | 구의 속성을 구성하는 목록입니다. 각 요소는 `{ position, radius, segment, color }` 객체로 구성됩니다. |

-   Description
    -   `position`([JSVector3D](../core/jsvector3d.md))이 포함되지 않으면 구 폴리곤이 생성되지 않습니다.
    -   속성에는 `radius`(number), `segment`(number), `color`([JSVector3D](../core/jscolor.md))가 포함됩니다.
    -   각 속성의 기본값은 `radius`(10), `segment`(30), `color`({255, 255, 255, 255}) 입니다.
    -   `radius`는 0.00005보다 큰 값, `segment`는 6보다 큰 값이 설정됩니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var polygon = Module.createPolygon("SPHERE");

var param = {
    position : new Module.JSVector3D(129.127, 35.17, 160.0),
    radius : 10,
    segment : 30,
    color : new Module.JSColor(255, 255, 255, 0)
};

polygon.setSphere(param);
```

{% endtab %}
{% endtabs %}

### setFaceTexture(index, id) → boolean

> 평면 객체를 구성하는 face에 이미지를 설정합니다.
>
> 입력 변수값(id)은 [loadTexture](jspolygon.md#loadTexture-id-url-boolean) API에 입력된 고유명칭 입니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| ----- | ------ | ------------ |
| index | number | face 인덱스. |
| id    | string | 고유 명칭.   |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   등록한 이미지 고유 명칭이 없는 경우.
        -   입력 변수값(index)이 평면 객체 face 갯수를 초과 또는 음수값이 설정된 경우.
-   Sample
    -   the init function 참조.
    -   [Sandbox_Polygon RTT](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_rtt_image_changing)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFireEffect(type) → boolean

> 평면 객체에 불 효과를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                              |
| ---- | ------- | -------------------------------------------------------- |
| type | boolean | <p>true: 불 효과 가시화(RTT).<br>false: 기본 가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   평면 객체 생성 실패한 경우.
-   Sample
    -   the createBurnEffectPolygon function 참조.
    -   [Sandbox_Fire Effect](https://sandbox.egiscloud.com/code/main.do?id=effect_fire)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setHeight(height) → boolean

> 평면 객체 생성 시 높이값을 가진 3d 객체를 생성합니다.
> 입력 변수값(height)은 0보다 큰값이 설정됩니다.
> 이 API는 기존에 `setPartCoordinates()` 또는 `setCoordinates()`로 정의된 객체에만 적용 가능합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description          |
| ------ | ------ | -------------------- |
| height | number | 객체 높이(in meter). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   평면 객체 생성 실패한 경우.
-   Sample
    -   the createPolygon function 참조.
    -   [Sandbox_Polygon Height](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_height)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setHeightByType(height, type) → boolean

> 평면 객체 생성 시 높이값을 가진 3d 객체를 생성합니다.
> 입력 변수값(type)은 윗면 정의 방법을 설정합니다.
> 이 API는 기존에 `setPartCoordinates()` 또는 `setCoordinates()`로 정의된 객체에만 적용 가능합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description          |
| ------ | ------ | -------------------- |
| height | number | 객체 높이(in meter).  |
| type   | number | <p>0: `setHeight()`(기존 방식) 사용(각 정점에서 일정 높이만큼 더함)<br>1: 윗면이 동일한 고도(height)가 되도록 보정</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   평면 객체 생성 실패한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setHeights(height) → boolean

> 평면 객체 생성 시 높이값을 가진 3d 객체를 생성합니다.
> 입력 변수값(height)은 0보다 큰값이 설정되며, 각 정점에 대한 높이를 설정합니다.
> 이 API는 기존에 `setPartCoordinates()` 또는 `setCoordinates()`로 정의된 객체에만 적용 가능합니다.


{% tabs %}
{% tab title="Information" %}

| Name   | Type                                | Description          |
| ------ | ----------------------------------- | -------------------- |
| height | [Collection](../core/collection.md) | 각 정점에 대한 높이(in meter). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   평면 객체 생성 실패한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setVerticalPlane(height, closed) → boolean

> 위가 뚫린 3D 객체(벽 폴리곤)를 생성합니다.
> 이 API는 기존에 `setPartCoordinates()` 또는 `setCoordinates()`로 정의된 객체에만 적용 가능합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type    | Description          |
| ------ | ------- | -------------------- |
| height | number  | 객체 높이(in meter).  |
| closed | boolean | 시작점과 끝점 연결 여부 |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   평면 객체 생성 실패한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.setVerticalPlane(50, true);
```

{% endtab %}
{% endtabs %}

### setFileMesh(path, name, pos) → boolean

> 모델 파일(3ds, xdo, 등)을 이용한 메쉬를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                                | Description                   |
| ---- | ----------------------------------- | ----------------------------- |
| path | string                              | 파일 경로                      |
| name | string                              | 파일 이름                      |
| pos  | [JSVector3D](../core/jsvector3d.md) | 생성 중심 좌표 (경도, 위도, 고도) |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   파일 경로가 없거나 너무 긴 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetTexturePlane(coordinates, parts, uv, texture, type) → boolean

> 텍스처 지정 폴리곤을 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                                            |
| ----------- | ------------------------------------- | ------------------------------------------------------ |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 정점 좌표 목록 (경도, 위도, 고도)                          |
| parts       | [Collection](../core/collection.md)   | 평면을 구성하는 coordinates 개수 목록                      |
| uv          | [JSVec2Array](../core/jsvec2array.md) | cordinates에 입력된 좌표 목록에 해당되는 uv 좌표 목록        |
| texture     | [JSIcon](../object/jsicon.md)         | 텍스쳐로 활용할 아이콘 객체                                |
| type        | boolean                               | <p>true: 지형 결합 가시화(RTT).<br>false: 기본 가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   정점 좌표가 2개 이하인 경우.
        -   part가 하나도 없는 경우.
        -   uv 좌표가 2개 이하인 경우.
        -   정점 좌표 개수와 uv 좌표 개수가 다른 경우

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetTexture(texture, faceIndex, type) → boolean

> 폴리곤에 텍스처를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                          | Description                                            |
| ----------- | ----------------------------- | ------------------------------------------------------ |
| texture     | [JSIcon](../object/jsicon.md) | 텍스쳐로 활용할 아이콘 객체                                |
| faceIndex   | number                        | face 인덱스                                             |
| type        | boolean                       | <p>true: 지형 결합 가시화(RTT).<br>false: 기본 가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   텍스처 객체가 없는 경우
        -   face 인덱스를 잘못 지정하는 경우

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetRenderToTexture(type) → boolean

> 지형 결합 가시화(RTT)를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                          | Description                                            |
| ----------- | ----------------------------- | ------------------------------------------------------ |
| type        | boolean                       | <p>true: 지형 결합 가시화(RTT).<br>false: 기본 가시화.</p> |

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setCullMode(type) → boolean

> 객체의 cull 모드를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                         | Description                                            |
| ----------- | ---------------------------- | ------------------------------------------------------ |
| type        | number                       | <p>1: none<br>2: cw<br>3: ccw</p> |

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPipe(center, radius, length, slice, color) → boolean

> 중심 좌표(경도, 위도, 고도)를 기준으로 원통 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                | Description                                       |
| ------ | ----------------------------------- | --------------------------------------------------|
| center | [JSVector3D](../core/jsvector3d.md) | 중심 좌표 (경도, 위도, 고도)                         |
| radius | number                              | 반지름 (in meter)                                  |
| length | number                              | 길이 (in meter)                                    |
| slice  | number                              | 단면의 다각수                                       |
| color  | [JSColor](../core/jscolor.md)       | 객체 색상  (기본값: 흰색 `rgba(255, 255, 255, 1)`) |

-   Description
    -   `radius`로 원통의 반지름을 설정합니다.
    -   `length`로 원통의 길이를 설정합니다.
    -   `slice`로 원통의 위/아래 면의 다각수를 설정합니다.
    -   `color`로 원통의 색상을 설정합니다.
    -   `radius`와 `length`가 너무 작거나, `slice`가 2 이하인 경우에는 원통이 생성되지 않습니다.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setExtraPosition(addLon, addLat, addHeight) → boolean

> 객체의 위치를 현재 위치에서 특정 좌표`(경도, 위도, 높이)`만큼 추가하여 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description         |
| --------- | ------ | ------------------- |
| addLon    | number | 추가적으로 이동할 경도 |
| addLat    | number | 추가적으로 이동할 위도 |
| addHeight | number | 추가적으로 이동할 높이 |

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.setExtraPosition(0.5, -1.5, 10.0);
```

{% endtab %}
{% endtabs %}

### move(lon, lat, alt) → boolean

> 객체의 위치를 특정 위치`(경도, 위도, 고도)`로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description    |
| ---- | ------ | -------------- |
| lon  | number | 이동할 경도 좌표 |
| lat  | number | 이동할 위도 좌표 |
| alt  | number | 이동할 고도 값   |

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.move(129.127, 35.17, 160.0);
```

{% endtab %}
{% endtabs %}

### moveAltitude(alt, type) → boolean

> 객체의 높이를 조절합니다.
> 입력 변수(type)에 따라 상대 이동 / 절대 이동을 구분합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description  |
| ---- | ------- | ------------ |
| alt  | number  | 이동할 고도 값 |
| type | boolean | <p>true: 목표 위치로 이동(절대 이동)<br>false: 입력 위치만큼 추가로 이동(상대 이동)</p> |

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.moveAltitude(100.0, true); // 절대 이동
polygon.moveAltitude(70.0, false); // 상대 이동
```

{% endtab %}
{% endtabs %}

### setRotation(x, y, z) → boolean

> 객체를 회전시킵니다.
> x, y, z 각 축을 기준으로 일정 각도 만큼 회전합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description      |
| ---- | ------- | ---------------- |
| x    | number  | x축 기준 회전 각도 |
| y    | number  | y축 기준 회전 각도 |
| z    | number  | z축 기준 회전 각도 |

-   Sample
    -   [Sandbox_Edit Polygon](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_edit)

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.setRotation(30.0, 45.0, 90.0); // x축 30도, y축 45도, z축 90도 회전
```

{% endtab %}
{% endtabs %}

### setScale(x, y, z) → boolean

> 객체의 크기를 조절합니다.
> x, y, z 각 축을 기준으로 일정 비율 만큼 확대/축소 합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description          |
| ---- | ------- | -------------------- |
| x    | number  | x축 기준 확대/축소 비율 |
| y    | number  | y축 기준 확대/축소 비율 |
| z    | number  | z축 기준 확대/축소 비율 |

-   Sample
    -   [Sandbox_Edit Polygon](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_edit)

{% endtab %}
{% tab title="Template" %}

```javascript
polygon.setScale(0.5, 1.5, 2.0); // x축 0.5배, y축 1.5배, z축 2배 확대/축소
```

{% endtab %}
{% endtabs %}

### getAxisEndpoint(axis, length) → [JSVector3D](../core/jsvector3d.md)

> 객체의 기준이 되는 축의 끝점 좌표를 반환합니다.
> 입력 변수(length)로 축의 길이를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type      | Description                     |
| ------ | ------- | ------------------------------- |
| axis   | number  | 반환할 축(0: x축, 1: y축, 2: z축) |
| length | number  | 축의 길이                        |

-   Sample
    -   [Sandbox_Edit Polygon](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_edit)

{% endtab %}
{% tab title="Template" %}

```javascript
let xvec = polygon.getAxisEndpoint(0, 200); // 객체 중심 기준 (200, 0, 0) 좌표 반환
```

{% endtab %}
{% endtabs %}

### getAltitude() → number

> 객체 중심의 고도를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    - [JSVector3D](../core/jsvector3d.md): 반환 성공
    - null: 반환 실패

{% endtab %}
{% tab title="Template" %}

```javascript
let alt = polygon.getAltitude();
```

{% endtab %}
{% endtabs %}


### setPartCoordinates(coordinates, parts) → boolean

> 평면 객체 생성에 필요한 정점 좌표 목록을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                            |
| ----------- | ------------------------------------- | -------------------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 정점 좌표 목록 (경도, 위도, 고도).     |
| parts       | [Collection](../core/collection.md)   | 평면을 구성하는 coordinates 개수 목록. |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   입력 변수값(coordinates) 구성요소가 없거나 정점 개수가 3개 이하인 경우.
        -   입력 변수값(parts) 구성요소가 없거나 입력 배열이 1개 이하인 경우.
-   Sample
    -   the createPolygon function 참조.
    -   [Sandbox_Polygon Height](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_height)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPlaneCoordinates(coordinates, altitude) → void

> 2차원 좌표로 평면 객체를 생성합니다.
> 입력 변수값(altitude)로 평면의 높이를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                            |
| ----------- | ------------------------------------- | -------------------------------------- |
| coordinates | [JSVec2Array](../core/jsvec2array.md) | 정점 좌표 목록 (경도, 위도).              |
| altitude    | number                                | 고도                                    |

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPartCoordinatesUV(coordinates, parts, uv, type) → boolean

> 평면 객체를 생성합니다.
>
> 입력 변수값(uv)로 평면에 이미지 표현 좌표를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                                                |
| ----------- | ------------------------------------- | ---------------------------------------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 정점 좌표 목록 (경도, 위도, 고도).                         |
| parts       | [Collection](../core/collection.md)   | 평면을 구성하는 coordinates 개수 목록.                     |
| uv          | [JSVec2Array](../core/jsvec2array.md) | cordinates에 입력된 좌표 목록에 해당되는 uv 좌표 목록.     |
| type        | boolean                               | <p>true: 지형 결합 가시화(RTT).<br>false: 기본 가시화.</p> |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   입력 변수값(coordinates) 구성요소가 없거나 정점 개수가 3개 이하인 경우.
        -   입력 변수값(parts) 구성요소가 없거나 입력 배열이 1개 이하인 경우.
        -   입력 변수값(uv) 구성요소가 없거나 입력 배열이 3개 이하인 경우.
        -   coordinates, uv 개수가 동일하지 않는 경우.
-   Sample
    -   the init function 참조.
    -   [Sandbox_Polygon RTT](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_rtt_image_changing)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPartCoordinatesCW(coordinates, parts, cw) → boolean

> 평면 객체를 생성합니다.
>
> 입력 변수값(cw)로 폴리곤의 방향을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                                                |
| ----------- | ------------------------------------- | ---------------------------------------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 정점 좌표 목록 (경도, 위도, 고도).                             |
| parts       | [Collection](../core/collection.md)   | 평면을 구성하는 coordinates 개수 목록.                         |
| cw          | boolean                               | <p>true: 시계 방향(CW).<br>false: 반시계 방향(CCW).</p>       |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
    -   실패 조건
        -   입력 변수값(coordinates) 구성요소가 없거나 정점 개수가 3개 이하인 경우.
        -   입력 변수값(parts) 구성요소가 없거나 입력 배열이 1개 이하인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFaceTextureWrapU(faceIndex, wrapType), setFaceTextureWrapV(faceIndex, wrapType) → boolean

> 타일링 텍스쳐 매핑 방식을 설정합니다(u, v).
>
> uv(텍스쳐) 좌표 범위(0.0 ~ 1.0)를 벗어난 영역에 대한 패턴을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     	| Type   | Description           |
| --------- | ------ | --------------------- |
| faceIndex | number | face 인덱스            |
| wrapType  | number | <p>0x2901: GL_REPEAT(이미지 반복)<br>0x8370: GL_MIRRORED_REPEAT(이미지 뒤집어서 반복)<br>0x812F: GL_CLAMP_TO_EDGE(0과 1 사이의 좌표 고정. 가장자리 패턴이 늘어남)</p> |

-   Return
    -   true : 설정 성공.
    -   false : 해당 face 인덱스를 가진 face가 없을 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### createVerticalGrid(layername, lefttop, rightbottom, row, col) → boolean

> 평면 그리드 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name        	| Type                                  | Description                                                |
| ----------- 	| ------------------------------------- | ---------------------------------------------------------- |
| layername 	| string 								| 레이어 이름.							                     |
| lefttop       | [JSVector3D](../core/jsvector3d.md)   | 좌측 상단 좌표.                     						 |
| rightbottom   | [JSVector3D](../core/jsvector3d.md) 	| 우측 하단 좌표.     										 |
| row        	| number                                | 새로 개수. 												 |
| col        	| number                                | 가로 개수. 												 |

-   Return
    -   true : 생성 성공.
    -   false : 생성된 객체가 없을 경우.
-   Sample
    -   function createVerticalPlane 참조.
    -   [Sandbox_Vertical_grid](https://sandbox.egiscloud.com/code/main.do?id=object_vertical_grid)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getCoordinates(), setCoordinates(coordinates) → [Collection](../core/collection.md)

> 평면 객체를 구성하는 좌표 목록을 설정합니다.
>
> 입력 변수값(coordinates)은 최소 3개 이상의 배열로 구성합니다.

{% tabs %}
{% tab title="Information" %}
| Name | Type | Description |
| ----------- | ----------------------------------- | -------------------------------------------------- |
| coordinates | [Collection](../core/collection.md) | 정점 좌표 목록 (경도, 위도, 고도). |

-   Return
    -   [Collection](../core/collection.md): 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var coorList = object.getCoordinates();
// ... or ...
var vertexList = Module.getMap().getInputPointList();
var object = Module.createPolygon("polygon");
object.setCoordinates(vertexList);
```

{% endtab %}
{% endtabs %}

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

### getStyle(), setStyle(style) → [JSPolygonStyle](jspolygonstyle.md)

> [JSPolygonStyle](jspolygonstyle.md)으로 적용된 스타일을 평면 객체에 설정합니다.
>
> 평면 객체의 색상, 투명도, 외곽선 등을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                | Description |
| ----- | ----------------------------------- | ----------- |
| style | [JSPolygonStyle](jspolygonstyle.md) | 속성 정보.  |

-   Return
    -   [JSPolygonStyle](jspolygonstyle.md): 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var objectStyle = polyLine.getStyle();
```

{% endtab %}
{% endtabs %}

### SetAnimationByID(id) → boolean

> GLTF 객체의 애니메이션을 ID 기준으로 설정합니다.  
> 평면 객체 타입이 GLTF 형식일 경우에만 동작합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description              |
| ---- | ------ | ------------------------ |
| id   | number | 애니메이션 ID (정수 값). |

-   Return  
    -   true: 설정 성공.  
    -   false: 설정 실패.  
        - 객체가 null이거나 GLTF 객체가 아닌 경우.  
        - 입력된 ID와 일치하는 애니메이션이 없는 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var gltfObject = Module.createPolygon("GLTF_OBJECT");
gltfObject.SetAnimationByID(0);
```

{% endtab %}
{% endtabs %}

### createWithFaces(parameter) → object

> Face 정보를 기반으로 평면 객체를 생성합니다.  
> 다각형을 Face 단위로 정의하고, 위치, 색상, 텍스처 좌표 등 세부 속성을 지정하여 생성할 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type   | Description                      |
| ---------- | ------ | -------------------------------- |
| parameter  | object | Face 기반 객체 정의 속성 정보.   |

- Return
  - object
    - result: 1 → 생성 성공 / 0 → 실패
    - name: `"JSPolygon.createWithFaces"`
    - return: 메시지

- 필수 속성
  - `position`: [longitude, latitude, altitude] 중심 좌표.
  - `faceInfo`: Face 배열. 각 Face는 다음과 같은 속성 포함:
    - `vertex`: [x, y, z, ...] 정점 배열.
    - `indexVertex`: [ [a, b, c], ... ] 정점 인덱스 배열.
    - `indexUV`: [ [a, b, c], ... ] 텍스처 좌표 인덱스 배열.
    - `uv`: [u, v, u, v, ...] 텍스처 좌표 배열.
    - `normal`: [x, y, z] 노멀 벡터.
    - `color`: 색상 (JSColor 형식).
    - `matrix`: 4x4 행렬 형식의 변환 매트릭스 (선택 사항).

- 선택 속성
  - `upVector`: `"y"` 또는 `"z"` (기본값: `"z"`).
  - `cullMode`: `"none"`, `"cw"`, `"ccw"` (기본값: `"ccw"`).
  - `moveOffset`: [x, y, z] 오프셋(meter 단위).
  - `vertexCombined`: boolean.

{% endtab %}
{% tab title="Template" %}

```javascript
const parameter = {
  position: [127.0, 37.5, 0],
  upVector: "z",
  cullMode: "ccw",
  faceInfo: [
    {
      vertex: [0, 0, 0, 1, 0, 0, 0, 1, 0],
      indexVertex: [[0, 1, 2]],
      indexUV: [[0, 1, 2]],
      uv: [0, 0, 1, 0, 0, 1],
      normal: [0, 0, 1],
      color: new Module.JSColor(255, 0, 0, 255),
      matrix: [
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
      ]
    }
  ]
};

const result = Module.createPolygon("F_POLY").createWithFaces(parameter);
console.log(result);
```

{% endtab %}
{% endtabs %}

### setHeightUV(uv, height) → boolean

> 평면 객체의 높이를 설정하고, 정점에 해당하는 텍스처 좌표(UV)를 지정하여 텍스처를 입힐 수 있는 3D 객체를 생성합니다.  
> 이 API는 기존에 `setPartCoordinates()` 또는 `setCoordinates()`로 정의된 객체에만 적용 가능합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                  | Description                           |
| ------ | ------------------------------------- | ------------------------------------- |
| uv     | [JSVec2Array](../core/jsvec2array.md) | 정점 텍스처 좌표 목록 (UV 좌표계).    |
| height | number                                | 객체 높이 (단위: meter, > 0).         |

- Return
  - `true` : 생성 성공.
  - `false` : 객체가 없거나 정점 정보가 없을 경우 실패.

- 제약 조건
  - 객체에 `setPartCoordinates()` 또는 `setCoordinates()`로 정점 정보가 먼저 설정되어 있어야 합니다.
  - `uv.get(i)` 는 `i`번째 정점에 대응됩니다.

{% endtab %}
{% tab title="Template" %}

```javascript
const uvList = new Module.JSVec2Array();
uvList.push(new Module.JSVector2D(0, 0));
uvList.push(new Module.JSVector2D(1, 0));
uvList.push(new Module.JSVector2D(0, 1));

const polygon = Module.createPolygon("TEX_POLY");
polygon.setCoordinates(vertexList);
polygon.setHeightUV(uvList, 20);
```

{% endtab %}
{% endtabs %}

### setOverlayObject(options) → boolean

> 오버레이 객체를 지도에 생성합니다.  
> 주어진 정점 정보와 스타일 옵션에 따라 평면 또는 선형 오버레이를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type     | Description |
| ------- | -------- | ----------- |
| options | object   | 오버레이 객체 옵션. 아래 속성 참고. |

**options 구조**

| Name       | Type                                  | Required | Description                                  |
| ---------- | ------------------------------------- | -------- | -------------------------------------------- |
| coordinate | [JSVec3Array](../core/jsvec3array.md) | ✔        | 객체를 구성하는 좌표 목록 (경도, 위도, 고도). 최소 3개 이상 필요. |
| style      | string                                | ✔        | 스타일 설정. `"polygon"` 또는 `"line"` 중 하나. |
| color      | [JSColor](../core/jscolor.md)         |          | 객체 색상. (기본값: 흰색 `rgba(255, 255, 255, 1)`) |

- Return  
  - `true` : 오버레이 생성 성공.  
  - `false` : 생성 실패 (좌표 부족, 잘못된 타입, 내부 오류 등).

- 제한 사항
  - `style`이 `"polygon"` 또는 `"line"`이 아닌 경우 무시됩니다.
  - `coordinate`는 최소 3개 이상의 점이 필요합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
const coords = new Module.JSVec3Array();
coords.push(new Module.JSVector3D(127.0, 37.5, 0));
coords.push(new Module.JSVector3D(127.1, 37.5, 0));
coords.push(new Module.JSVector3D(127.1, 37.6, 0));

const poly = Module.createPolygon("OVERLAY_POLYGON");
poly.setOverlayObject({
    coordinate: coords,
    style: "polygon",
    color: new Module.JSColor(255, 255, 0, 0)
});
```

{% endtab %}
{% endtabs %}

### getUnionMode(), setUnionMode(bMode) → void

> 폴리곤 객체의 연산 모드를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description |
|--------|--------|-------------|
| bMode  | boolean | `true`: 평면 연산 모드(`EOT_PLANE`), `false`: 입체 연산 모드(`EOT_POLYHEDRON`) |

- Return  
  - 없음 (void)

- Description  
  - 폴리곤 객체의 연산 방식을 설정합니다.  
  - `true`로 설정하면 내부 객체 타입이 `EOT_PLANE`으로 설정되어 평면 병합 연산을 수행하며,  
    `false`로 설정하면 `EOT_POLYHEDRON`으로 처리되어 입체 병합 연산이 가능합니다.  
  - 설정 이후 RTT(렌더 타겟 텍스처) 갱신 플래그가 활성화됩니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSPolygon : Module.getPolygon()
};

// 평면 병합 연산 모드 설정
API.JSPolygon.setUnionMode(true);

// 입체 병합 연산 모드 설정
API.JSPolygon.setUnionMode(false);
```
{% endtab %}
{% endtabs %}

### Type Definitions

#### JSPolygon.loadFileOption

> 3ds 포맷 파일을 이용하여 평면 객체를 생성합니다.

| Name     | Type                                | Attributes | Default | Description                        |
| -------- | ----------------------------------- | ---------- | ------- | ---------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) |            |         | 생성 중심 좌표 (경도, 위도, 고도). |
| url      | string                              |            |         | 3ds 요청 url.                      |
| align    | string                              |            |         | 정렬 옵션.                         |
