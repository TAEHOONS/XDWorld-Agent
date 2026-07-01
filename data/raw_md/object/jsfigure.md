---
description: 지도 내 3D figure 객체 생성 및 설정하기 위한 API 입니다.
---

# JSFigure

> Module.createFigure() API를 생성합니다.
>
> [JSFigure Type Constants](../etc/type-list.md#jsfigure-type-list)

```javascript
let figure = Module.createFigure("ID");
```

## Properties

| Name     			| Type                                	| Description           |
| ----------------- | ------------------------------------- | --------------------- |
| isplayer 			| boolean                             	| 비디오 실행 여부. 			|
| videoStreaming 	| boolean                             	| 비디오 스트리밍 여부. 		|
| axisX 			| boolean                             	| 좌우 반전. 				|
| axisY 			| boolean                             	| 상하 반전. 				|

## Function

### getAngle() → number

> 객체의 Y축 중심 회전 각도(degree 단위)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 반환 성공.
    -   -999.0: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var dAngle = figure.getAngle();
```

{% endtab %}
{% endtabs %}

### getBoundary() → [JSAABBox3D](../core/jsaabbox3d.md)

> 객체의 공간 영역 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSAABBox3D](../core/jsaabbox3d.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var boundary = figure.getBoundary();
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
var vCenter = figure.getCenter();
var dCenterLon = vCenter.Longitude;
var dCenterLat = vCenter.Latitude;
var dCenterAlt = vCenter.Altitude;
```

{% endtab %}
{% endtabs %}

### getExtent() → number

> 객체의 공간 영역의 장축 거리를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 거리 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var bExtends = figure.getExtent();
```

{% endtab %}
{% endtabs %}

### getFigureType() → number

> 객체의 figure 타입을 반환합니다.
>
> [JSFigure Type Constants](../etc/type-list.md#jsfigure-type-list)

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 반환 성공.
    -   -1: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var figureType = figure.getFigureType();
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

### getPosition() → [JSVector3D](../core/jsvector3d.md)

> 객체의 바닥면 중심 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let position = figure.getPosition();
let longitude = position.x;
let latitude = position.y;
let altitude = position.z;
```

{% endtab %}
{% endtabs %}

### getSize() → [JSVector3D](../core/jsvector3d.md)

> 객체의 해당되는 3차원 축의 크기(meter 단위)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let size = figure.getSize();
let width = size.x;
let height = size.y;
let depth = size.z;
```

{% endtab %}
{% endtabs %}

### setAngle(angle) → boolean

> 객체의 Y축 중심 회전 각도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description              |
| ----- | ------ | ------------------------ |
| angle | number | 회전 각도 (degree 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   입력 변수값(angle)이 0 ~ 360 범위를 벗어난 값이 입력된 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
figure.setAngle(50.0);
```

{% endtab %}
{% endtabs %}

### setDepth(depth) → boolean

> 객체의 Z축 깊이를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description |
| ----- | ------ | ----------- |
| depth | number | 깊이 값.    |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
figure.setDepth(200.0);
```

{% endtab %}
{% endtabs %}

### setHeight(height) → boolean

> 객체의 Y축 높이를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| height | number | 높이(meter 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
figure.setHeight(100.0);
```

{% endtab %}
{% endtabs %}

### setWidth(width) → boolean

> 객체의 X축 너비를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description       |
| ----- | ------ | ----------------- |
| width | number | 너비(meter 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
figure.setWidth(130.0);
```

{% endtab %}
{% endtabs %}

### setPosition(position) → boolean

> 객체의 바닥면 중심 좌표(경도, 위도, 고도)를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                         |
| :------- | :---------------------------------- | :---------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 바닥면 중심 위치(경도, 위도, 고도). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var vPos = new Module.JSVector3D("127.0273188", "37.4977981", "30.0");
figure.setPosition(vPos);
```

{% endtab %}
{% endtabs %}

### setSize(width, height, depth) → boolean

> 객체의 해당되는 3차원 축의 크기(meter 단위)를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| :----- | :----- | :---------------- |
| width  | number | 너비(meter 단위). |
| height | number | 높이(meter 단위). |
| depth  | number | 깊이(meter 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
figure.setSize(50.0, 100.0, 150.0);
```

{% endtab %}
{% endtabs %}

### setledBoard(option) → string

> 전광판 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |
| url      		| string                            | 미디어 URL 경로.			|
| streaming 	| boolean 							| 비디오 스트리밍 설정. 		|
| xaxis      	| boolean                           | 좌우 반전 설정.           	|
| yaxis     	| boolean                           | 상하 반전 설정.			|

-   Return
    -   success : 텍스쳐 생성 성공.
    -   실패 조건
        -   null : 생성된 객체가 없을 경우.
        -   url tag isn't exist : url 태그가 없을 경우.
        -   streaming tag isn't exist. : streaming 태그가 없을 경우.
-   Sample
    -   function createBoard 참조.
    -   [Sandbox_LED Display](https://sandbox.egiscloud.com/code/main.do?id=object_ledboard)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### createPlane(min, max) → boolean

> 평면 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |
| min      		| [JSVector3D](../core/jsvector3d.md) | 입력된 영역의 좌상단 좌표.			|
| max 			| [JSVector3D](../core/jsvector3d.md) | 입력된 영역의 우하단 좌표. 		|

-   Return
    -   true : 객체 생성 성공.
    -   false : 생성된 객체가 없을 경우.
-   Sample
    -   function createPlane 참조.
    -   [Sandbox_Image_overlap](https://sandbox.egiscloud.com/code/main.do?id=object_image_overlap)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### editPlane() → boolean

> 평면 객체를 편집상태로 전환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true : 텍스쳐 생성 성공.
    -   false : 생성된 객체가 없을 경우.
-   Sample
    -   function editplane 참조.
    -   [Sandbox_Image_overlap](https://sandbox.egiscloud.com/code/main.do?id=object_image_overlap)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### createOverlapRTT(option) → boolean

> 이미지 오버랩을 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |
| option 		| boolean 							| 지형 성절토 여부. 		|

-   Return
    -   true : 이미지 오버랩 생성 성공.
    -   false :
        -   생성된 객체가 없을 경우.
        -   입력된 좌표가 4개가 아닐 경우
-   Sample
    -   function insertOverlapRTT 참조.
    -   [Sandbox_Image_overlap](https://sandbox.egiscloud.com/code/main.do?id=object_image_overlap)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### clearTexture() → boolean

> 객체에 입력된 텍스쳐를 삭제합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |

-   Return
    -   true : 텍스쳐 삭제 성공.
    -   false : 생성된 객체가 없을 경우.
-   Sample
    -   function clearObject 참조.
    -   [Sandbox_Image_overlap](https://sandbox.egiscloud.com/code/main.do?id=object_image_overlap)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setInfo(option) → boolean

> 현재 객체 정보를 입력합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |
| position 		| [JSVector3D](../core/jsvector3d.md)	| 객체 위치 좌표. 	|
| size 			| [JSVector3D](../core/jsvector3d.md)	| 객체 크기. 		|
| angle 		| [JSVector3D](../core/jsvector3d.md)	| 객체 회전 각도. 	|
| color 		| [JSColor](../core/jscolor.md)			| 객체 색상. 		|
| imagesize 	| [Size2D](../etc/tag-list.md#size2d-style-type) | 이미지 길이. 	|
| imagedata 	| string								| 이미지 데이터. 		|

-   Return
    -   true : 객체 정보 입력 성공.
    -   false : 
		-	생성된 객체가 없을 경우.
		-	이미지 데이터가 없을 경우.
-   Sample
    -   function importData 참조.
    -   [Sandbox_Image_overlap](https://sandbox.egiscloud.com/code/main.do?id=object_image_overlap)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getInfo() → string

> 객체 정보를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |

-   Return
    -   position : 객체 위치.
    -   size : 객체 크기.
    -   angle : 객체 회전 각도.
    -   color : 객체 색상.
-   Sample
    -   function exportData 참조.
    -   [Sandbox_Image_overlap](https://sandbox.egiscloud.com/code/main.do?id=object_image_overlap)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getRectInfo() → object

> 객체의 좌표정보를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description           |
| :------------ | :-------------------------------- | :-------------------- |

-   Return
    -   leftTop : 좌상단 좌표.
    -   rightTop : 우상단 좌표.
    -   leftBottom : 좌하단 좌표.
    -   rightBottom : 우하단 좌표.
-   Sample
    -   function exportData 참조.
    -   [Sandbox_Get_Figure_Coordinate](https://sandbox.egiscloud.com/code/main.do?id=object_figure_coordinate)

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

### getStyle(), setStyle(style) → [JSPolygonStyle](./jspolygonstyle.md)

> [JSPolygonStyle](./jspolygonstyle.md)에 적용된 객체의 스타일을 설정합니다.
>
> 적용 가능한 스타일(업데이트 될 수 있음 [JSPolygonStyle](./jspolygonstyle.md))

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                  | Description  |
| ----- | ------------------------------------- | ------------ |
| style | [JSPolygonStyle](./jspolygonstyle.md) | 객체 스타일. |

-   Return
    -   ([JSPolygonStyle](./jspolygonstyle.md)): 설정 성공.
    -   null: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var figure = new Module.JSFigure();
var figureStyle = figure.getStyle();
// ... or ...
var figure = new Module.JSFigure();
var figureStyle = new Module.JSFigureStyle();
//...
figure.setStyle(figureStyle);
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
