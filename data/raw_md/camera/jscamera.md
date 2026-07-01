---
description: 지도 카메라 설정을 위한 API입니다.
---

# JSCamera

> Module.getViewCamera API를 생성합니다.

```javascript
var camera = Module.getViewCamera();
```

## Properties

| Name     				| Type                                	| Description                   |
| --------------------- | ------------------------------------- | ----------------------------- |
| videoStreaming     	| boolean                              	| 비디오 스트리밍 여부.               	|
| videoFar     			| number                              	| 비디오 최대 가시거리.              	|
| videoFovX      		| number                              	| 화각 넓이.               			|
| videoFovY     		| number                              	| 화각 높이.               			|
| videoAlpha     		| number                              	| 비디오 투명값.                   	|
| videoAxisX     		| boolean                              	| 좌우 반전.                   		|
| videoAxisY    		| boolean                              	| 상하 반전.               			|
| videoZoom    			| number                             	| 비디오 배율.                   	|
| videoFarPlane    		| boolean                             	| 비디오 뒷배경 여부.                  |
| videoResolution 		| number 								| 비디오 해상도.  					|
| videoObjectMapping   	| boolean                              	| 건물 매핑 여부.                 	|
| videoIsplayer 		| boolean                            	| 비디오 재생 여부.        			|

## Function

### AltitudeDown()

> 카메라의 고도를 낮춥니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.AltitudeDown();
```

{% endtab %}
{% endtabs %}

### AltitudeUp()

> 카메라의 고도를 높입니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.AltitudeUp();
```

{% endtab %}
{% endtabs %}

### AngleDown()

> 카메라의 기울기 각도를 낮춥니다.
>
> 회전을 지원하지 않는 평면 모드에서는 작동하지 않습니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.AngleDown();
```

{% endtab %}
{% endtabs %}

### AngleUp()

> 카메라의 기울기 각도를 높입니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.AngleUp();
```

{% endtab %}
{% endtabs %}

### FOVDecrease()

> 카메라의 FOV를 줄입니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().FOVDecrease();
```

{% endtab %}
{% endtabs %}

### FOVIncrease()

> 카메라의 FOV를 높입니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().FOVIncrease();
```

{% endtab %}
{% endtabs %}

### getMapZoomLevel() → number

> 카메라 고도에서 가시화 된 지형 정밀 레벨 정보를 반환합니다.

{% tabs %}

{% tab title="Information" %}

-   Return
    -   number: 현재 가시화 지형 레벨.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var ZoomLevel= API.JSCamera.getMapZoomLevel();
```

{% endtab %}
{% endtabs %}

### getMapScale() → number

> 직교 투영시 축척을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 1cm에 대한 축척.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var mapScale= API.JSCamera.getMapScale();
```

{% endtab %}
{% endtabs %}

### setLookAt(f_altitude, f_longitude, f_latitude, t_altitude, t_longitude, t_latitude) → boolean

> 두 점을 사용하여 카메라를 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                | Description                                |
| ----------- | ------ | ------------------------------------------ |
| f_altitude  | number | 카메라 위치 고도 좌표 (degrees 단위).          |
| f_altitude  | number | 카메라 위치 고도 좌표 (degrees 단위).          |
| f_longitude | number | 카메라 위치 경도 좌표 (degrees 단위).          |
| f_latitude  | number | 카메라 위치 위도 좌표 (degrees 단위).          |
| t_altitude  | number | 카메라가 보고 있는 위치 고도 좌표(degrees 단위). |
| t_longitude | number | 카메라가 보고 있는 위치 경도 좌표(degrees 단위). |
| t_latitude  | number | 카메라가 보고 있는 위치 위도 좌표(degrees 단위). |
-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setLookAt(129.128265, 35.171834, 500.0, 129.128265, 35.161834, 10.0);
```

{% endtab %}
{% endtabs %}

### look(from, to) → boolean

> 두 점을 사용하여 카메라를 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                                | Description                                     |
| ---- | ----------------------------------- | ----------------------------------------------- |
| from | [JSVector3D](../core/jsvector3d.md) | 카메라 위치 좌표 (경도, 위도, 고도).            |
| to   | [JSVector3D](../core/jsvector3d.md) | 카메라가 보고 있는 위치 좌표(경도, 위도, 고도). |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function init 참조.
    -   [Sandbox_Circular Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_round_path)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().look(new Module.JSVector3D(129.128265, 35.171834, 500.0), new Module.JSVector3D(129.128265, 35.161834, 10.0));
```

{% endtab %}
{% endtabs %}

### getLookPosition(distance) → [JSVector3D](../core/jsvector3d.md)

> 카메라가 바라보는 점의 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description                        |
| -------- | ------ | ---------------------------------- |
| distance | number | 카메라에서부터 바라보는 지점까지의 거리. |

-   Return
    -   [JSVector3D](../core/jsvector3d.md) : 카메라가 보는 방향으로 distance 만큼 진행한 좌표.

{% endtab %}
{% tab title="Template" %}

```javascript
var lookPosition = Module.getViewCamera().getLookPosition();
```

{% endtab %}
{% endtabs %}

### setSmoothMove(type) → void

> 카메라의 부드러운 움직임을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                         |
| -----| ------- | --------------------------------------------------- |
| type | boolean | <p>Smooth Move<br>true: 활성화<br>false: 비활성화</p> |

-   Description
    -   카메라 이동 시 현재 위치와 다음 위치 사이를 보간하여 더 자연스러운 움직임을 구현합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setSmoothMove(true); // 활성화(기본값)
Module.getViewCamera().setSmoothMove(false); // 비활성화
```

{% endtab %}
{% endtabs %}

### MapRender()

> 3D 지도 화면을 갱신합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().MapRender();
```

{% endtab %}
{% endtabs %}

### move(position, tilt, direct, speed)

> 카메라를 지정된 위치, 기울기, 방향을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                          |
| -------- | ----------------------------------- | ------------------------------------ |
| position | [JSVector3D](../core/jsvector3d.md) | 카메라 위치 좌표 (경도, 위도, 고도). |
| tilt     | number                              | 카메라 기울기.                       |
| direct   | number                              | 카메라 좌우 회전.                    |
| speed    | number                              | 카메라 이동 속도 (1.0 ~ 10.0).       |

-   Sample
    -   function init 참조.
    -   [Sandbox_Position Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_position)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().move(new Module.JSVector3D(129.128265, 35.171834, 500.0), 70, 0, 0);
```

{% endtab %}
{% endtabs %}


### moveDist(location, tilt, direct, dist, speed)

> 카메라를 지정된 위치, 기울기, 방향, 거리, 속도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                          |
| -------- | ----------------------------------- | ------------------------------------ |
| location | [JSVector3D](../core/jsvector3d.md) | 카메라 위치 좌표 (경도, 위도, 고도). |
| tilt     | number                              | 카메라 기울기.                       |
| direct   | number                              | 카메라 좌우 회전.                    |
| dist     | number                              | (현재 미적용).                       |
| speed    | number                              | 카메라 이동속도 (기본 1).            |

{% endtab %}

{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var vTargetPos = new Module.JSVector3D(longitude, latitude, altitude);
API.JSCamera.moveDist(vTargetPos, 45.0, 90.0, 1, 0.0);
```

{% endtab %}
{% endtabs %}

### MoveDown()

> 카메라를 현재 위치에서 뒤로 이동합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveDown();
```

{% endtab %}
{% endtabs %}

### MoveLeft()

> 카메라를 현재 위치에서 왼쪽으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveLeft();
```

{% endtab %}
{% endtabs %}

### moveLonLat(longitude, latitude)

> 카메라를 지정된 위치(경도, 위도)를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| longitude | number | 카메라 위치 경도 좌표 (degrees 단위). |
| latitude  | number | 카메라 위치 위도 좌표 (degrees 단위). |

{% endtab %}

{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveLonLat(127.0273188, 37.4977981);
```

{% endtab %}
{% endtabs %}

### moveLonLatAlt(x, y, z, type)

> 카메라를 지정된 위치(경도, 위도, 고도)를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                           |
| ---- | ------- | ------------------------------------- |
| x    | number  | 카메라 위치 경도 좌표 (degrees 단위). |
| y    | number  | 카메라 위치 위도 좌표 (degrees 단위). |
| z    | number  | 카메라 위치 고도 좌표 (meter 단위).   |
| type | boolean | 카메라 이동 애니메이션 적용 유무.     |

-   Sample
    -   function init 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
var height = Module.getMap().getTerrHeight(126.92836647767662, 37.52439503321471);
```

{% endtab %}
{% endtabs %}

### moveLonLatAltOval(longitude, latitude, altitude, speed)

> 카메라를 지정된 위치(경도, 위도, 고도) 이동 시 확대/축소 애니메이션을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| longitude | number | 카메라 위치 경도 좌표 (degrees 단위). |
| latitude  | number | 카메라 위치 위도 좌표 (degrees 단위). |
| altitude  | number | 카메라 위치 고도 좌표 (meter 단위).   |
| speed     | number | 카메라 이동속도 (기본 1).             |

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveLonLatAltOval(127.0273188, 37.4977981, 500.0, 1);
```

{% endtab %}
{% endtabs %}

### moveLonLatBoundary(min, max) → boolean

> 최소 좌표점, 최대 좌표점을 이용한 카메라 이동 및 완료 이벤트를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                                | Description         |
| ---- | ----------------------------------- | ------------------- |
| min  | [JSVector2D](../core/jsvector2d.md) | 2차원 경위도 min 좌표 |
| max  | [JSVector2D](../core/jsvector2d.md) | 2차원 경위도 max 좌표 |

- Return
    - true : 설정 성공.
    - false : 설정 실패

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var Boundary = {
    min : new Module.JSVector2D(min_longitude, min_latitude);
    max : new Module.JSVector2D(max_longitude, max_latitude);
}
API.JSCamera.moveLonLatBoundary(Boundary.min, Boundary.max);
```

{% endtab %}
{% endtabs %}

### moveLonLatBoundarybyJson(option) → string

> 최소 좌표점, 최대 좌표점을 이용한 카메라 이동 및 완료 이벤트를 설정합니다.

{% tabs %}

{% tab title="Information" %}

| Name   | Type                                                                   | Description |
| ------ | ---------------------------------------------------------------------- | ----------- |
| option | [JSCamera.MoveBoundaryOption](jscamera.md#jscamera.moveboundaryoption) | 속성 정보.  |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
    -   실패 조건
        -   [JSCamera.MoveBoundaryOption](jscamera.md#jscamera.moveboundaryoption) 구성 태그가 누락된 경우.
-   Sample
    -   function moveTestArea 참조.
    -   [Sandbox_Camera Area Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set_viewrect)

{% endtab %}
{% tab title="Template" %}

```javascript
function complete(...args) {
    console.log(args);
}

let json = {
    boundary: {
        // Camera movement position
        min: new Module.JSVector2D(area_min_lon, area_min_lat), // Bottom left
        max: new Module.JSVector2D(area_max_lon, area_max_lat), // Top right
    },
    complete: complete, // Callback after movement completion
};
```

{% endtab %}
{% endtabs %}

### moveLonLatOval(longitude, latitude, speed)

> 카메라를 지정된 위치(경도, 위도) 이동 시 애니메이션 효과를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| longitude | number | 카메라 위치 경도 좌표 (degrees 단위). |
| latitude  | number | 카메라 위치 위도 좌표 (degrees 단위). |
| speed     | number | 카메라 이동속도 (기본 1).             |

{% endtab %}

{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveLonLatOval(127.0273188, 37.4977981, 1);
```

{% endtab %}
{% endtabs %}

### moveOval(position, tilt, direct, speed)

> 카메라를 지정된 위치(경도, 위도, 고도) 이동 시 애니메이션 효과를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                          |
| -------- | ----------------------------------- | ------------------------------------ |
| position | [JSVector3D](../core/jsvector3d.md) | 카메라 위치 좌표 (경도, 위도, 고도). |
| tilt     | number                              | 카메라 기울기.                       |
| direct   | number                              | 카메라 좌우 회전.                    |
| speed    | number                              | 카메라 이동 속도 (1.0 ~ 10.0).       |

-   Sample
    -   function initPage 참조.
    -   [Sandbox_Landscape View](https://sandbox.egiscloud.com/code/main.do?id=camera_landscape)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().moveOval(new Module.JSVector3D(129.128265, 35.171834, 500.0), 70, 0, 1);
```

{% endtab %}
{% endtabs %}

### moveOvalDist(location, tilt, Direct, speed)

> 카메라를 지정된 위치(경도, 위도, 고도)로 부터 기울기 방향을 기준으로 거리를 적용한 좌표를 설정한다.
>
> 카메라 이동시 확대/축소 애니메이션 효과 설정한다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                          |
| -------- | ----------------------------------- | ------------------------------------ |
| location | [JSVector3D](../core/jsvector3d.md) | 카메라 위치 좌표 (경도, 위도, 고도). |
| tilt     | number                              | 카메라 기울기.                       |
| direct   | number                              | 카메라 좌우 회전.                    |
| speed    | number                              | 카메라 이동 속도 (1.0 ~ 10.0).       |

{% endtab %}

{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var vTargetPos = new Module.JSVector3D(longitude, latitude, altitude);
API.JSCamera.moveOvalDist(vTargetPos, 45.0, 90.0, 0.0, 1);
```

{% endtab %}
{% endtabs %}

### MoveRight()

> 카메라를 현재 위치에서 오른쪽으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveRight();
```

{% endtab %}
{% endtabs %}

### MoveUp()

> 카메라를 현재 위치에서 앞으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveUp();
```

{% endtab %}
{% endtabs %}

### pauseAutoMove(pause) → boolean

> 카메라 자동 이동 시 일시 중지를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    | Description                                           |
| ----- | ------- | ----------------------------------------------------- |
| pause | boolean | <p>자동 이동 설정.<br>true: 멈춤.<br>false: 시작.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function pauseCameraAutoMove 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().pauseAutoMove(true);
```

{% endtab %}
{% endtabs %}

### reset()

> 카메라의 속성 정보를 초기화 상태로 설정합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().reset();
```

{% endtab %}
{% endtabs %}

### rotateLeft()

> 카메라를 현재 왼쪽으로 회전합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.rotateLeft();
```

{% endtab %}
{% endtabs %}

### rotateRight()

> 카메라를 현재 오른쪽으로 회전합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.rotateRight();
```

{% endtab %}
{% endtabs %}

### getDistance(), setDistance(Dist) → number

> 카메라 시점, 위치 간의 거리를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                     |
| ---- | ------ | ------------------------------- |
| Dist | number | 카메라 시야 거리 (meters 단위). |

{% endtab %}
{% tab title="Template" %}

```javascript
var dist = Module.getViewCamera().getDistance();
Module.getViewCamera().setDistance(500.0);
```

{% endtab %}
{% endtabs %}

### setAutoMovePosition(coordinates) → boolean

> 카메라의 자동 이동 좌표 목록을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                 |
| ----------- | ------------------------------------- | --------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 자동 이동 경로의 좌표 목록. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function setAutoMovePosition 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
var vMovePositionList = new Module.JSVec3Array();
vMovePositionList.push(new Module.JSVector3D(129.12695440075726, 35.16601614946393, 50.0));
vMovePositionList.push(new Module.JSVector3D(129.12188858001704, 35.173578909363805, 50.0));
vMovePositionList.push(new Module.JSVector3D(129.12027302076595, 35.17489727168604, 50.0));
vMovePositionList.push(new Module.JSVector3D(129.1193336034672, 35.176296224587475, 50.0));
Module.getViewCamera().setAutoMovePosition(vMovePositionList);
```

{% endtab %}
{% endtabs %}

### insertAutoMovePosition(coordinates, direct, tilt) → boolean

> 카메라의 자동 이동 좌표 목록에 새로운 좌표를 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                | Description                                     |
| ----------- | ----------------------------------- | ----------------------------------------------- |
| coordinates | [JSVector3D](../core/jsvector3d.md) | 추가할 좌표. 경도, 위도, 고도로 구성. (degrees 단위) |
| tilt        | number                              | 카메라의 상하 기울기 각도 (단위: 도, degree).        |
| direct      | number                              | 카메라의 방위각, 즉 수평 방향 (단위: 도, degree)     |


-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var movePosition = new Module.JSVector3D(129.12695440075726, 35.16601614946393, 50.0);
Module.getViewCamera().insertAutoMovePosition(movePosition, 90, 45);
```

{% endtab %}
{% endtabs %}

### setAutoMoveWaitFrame(speed) → boolean

> 카메라의 자동 이동 중 카메라의 이동 간격 발생 프레임을을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                            |
| ----- | ------ | -------------------------------------- |
| speed | number | 카메라 이동 애니메이션 발생 프레임 수. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function setAutoMovePosition 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setAutoMoveWaitFrame(3);
```

{% endtab %}
{% endtabs %}

### SetAutoMoveIntrerval(interval) → boolean

> 카메라의 자동 이동 중 카메라의 한 구간 이동 간격을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description            |
| -------- | ------ | ---------------------- |
| interval | number | 카메라 한 구간 이동 간격. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().SetAutoMoveIntrerval(0.01);
```

{% endtab %}
{% endtabs %}

### setAutoMoveRoundPositions(center, distance, altitude, startAngle, endAngle, type) → boolean

> 카메라의 원형 이동 경로를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type                                | Description                                                 |
| ---------- | ----------------------------------- | ----------------------------------------------------------- |
| center     | [JSVector3D](../core/jsvector3d.md) | 카메라 회전 중심 좌표(경도, 위도, 고도)                     |
| distance   | number                              | 카메라 회전 반지름 거리 (meter 단위).                       |
| altitude   | number                              | 카메라 위치 고도 좌표 (meter 단위).                         |
| startAngle | number                              | 카메라 초기 시야 방향                                       |
| endAngle   | number                              | 카메라 종료 시야 방향                                       |
| type       | boolean                             | 카메라 이동 방향 설정 (true: 반시계 방향, false: 시계 방향) |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function setAutoMovePosition 참조.
    -   [Sandbox_Circular Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_round_path)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setAutoMoveRoundPositions(new Module.JSVector3D(129.12732457984308, 35.171000072302796, 4.0), 400.0, 350.0, -130.0, -160.0, true);
```

{% endtab %}
{% endtabs %}

### SetCameraShakeEffect(type) → boolean

> 카메라 흔들림 효과를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description              |
| ---- | ------- | ------------------------ |
| type | boolean | 카메라 흔들링 유무 설정. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function ShakeCamera 참조.
    -   [Sandbox_Camera Shake](https://sandbox.egiscloud.com/code/main.do?id=camera_quake)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().SetCameraShakeEffect(true);
```

{% endtab %}
{% endtabs %}

### SetCameraShakeStrength(value) → boolean

> 카메라 흔들림 강도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                   |
| ----- | ------ | ----------------------------- |
| value | number | 카메라 흔들링 강도 (1 ~ 100). |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function SetShakeEffectStrength 참조.
    -   [Sandbox_Camera Shake](https://sandbox.egiscloud.com/code/main.do?id=camera_quake)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().SetCameraShakeStrength(50);
```

{% endtab %}
{% endtabs %}

### setPermitUnderGround(type)

> 지하에서 카메라 이동 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                               |
| ---- | ------- | --------------------------------------------------------- |
| type | boolean | <p>지하 이동<br>true: 이동 가능.<br>false: 이동 금지.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript
Module.getViewCamera().setPermitUnderGround(true);
```

{% endtab %}
{% endtabs %}

### startAutoMove() → boolean

> 카메라 자동 이동을 시작합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function startCameraAutoMove 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().startAutoMove();
```

{% endtab %}
{% endtabs %}

### stopAutoMove() → boolean

> 카메라 자동 이동을 종료합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function stopCameraAutoMove 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().stopAutoMove();
```

{% endtab %}
{% endtabs %}

### viewNorth()

> 카메라가 정복 방향을 바라보도록 회전 합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.viewNorth();
```

{% endtab %}
{% endtabs %}

### ZoomIn()

> 화면 중심 위치를 기준으로 카메라 확대를 실행합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.ZoomIn();
```

{% endtab %}
{% endtabs %}

### ZoomOut()

> 화면 중심 위치를 기준으로 카메라 축소를 실행합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.ZoomOut();
```

{% endtab %}
{% endtabs %}

### Zoom(screenX, screenY, distance)

> 화면 특정 좌표를 기준으로 카메라 확대/축소를 실행합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description                                |
| -------- | ------ | ------------------------------------------ |
| screenX  | number | 화면의 X 좌표(정수)                          |
| screenY  | number | 화면의 Y 좌표(정수)                          |
| distance | number | 확대/축소 거리. 양수면 줌아웃, 음수면 줌인.      |

- Return
    - true: 확대/축소 성공
    - false: 확대/축소 실패

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.Zoom(0, 0, 100.0); // Zoom Out
API.JSCamera.Zoom(0, 0, -100.0); // Zoom In
```

{% endtab %}
{% endtabs %}

### setVideoInfo(option) → string

> 비디오 텍스쳐를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     		| Type                              | Description               |
| :------------ | :-------------------------------- | :------------------------ |
| url      		| string                            | 미디어 URL 경로.              	|
| dronemode 	| boolean | 중심 좌표 (경도, 위도, 고도). 	| 드론 모드 설정.				|
| streaming     | boolean                           | 비디오 스트리밍 설정.             |
| objectmapping | boolean                           | 건물 매핑 설정.               	|
| alpha      	| number                           	| 비디오 투명값 설정.              |
| zoom     		| number                            | 비디오 배율 설정.               |
| fov     		| [Size2D](../etc/tag-list.md#size2d-style-type)                            | 비디오 화각 설정.               |
| xaxis			| boolean                           | 비디오 좌우 반전 설정.           	|
| yaxis    		| boolean                           | 비디오 상하 반전 설정.            |
| resolution    | number                            | 비디오 해상도 설정.              |
| farplane    	| boolean                           | 뒷배경 설정.               	|

-   Return
    -   success : 텍스쳐 생성 성공.
    -   실패 조건
        -   url tag isn't exist : url 태그가 없을 경우.
        -   streaming tag isn't exist : streaming 태그가 없을 경우.
-   Sample
    -   function createCCTV, createCCTVDrone 참조.
    -   [Sandbox_Video Texture](https://sandbox.egiscloud.com/code/main.do?id=camera_video_texture)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### clearVideo() → boolean

> 비디오 텍스쳐를 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true : 초기화 성공.
    -   false : 초기화 실패.
    -   실패 조건
        -   비디오 텍스쳐가 없을 경우.
        -   비디오 데이터가 없을 경우.
        -   비디오 경로가 없을 경우.
-   Sample
    -   See function setTilt.
    -   [Sandbox_Video Texture](https://sandbox.egiscloud.com/code/main.do?id=camera_video_texture)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}


## Getter / Setter

### getAnimationSpeed(), setAnimationSpeed(speed) → number

> 카메라 이동 애니메이션의 속도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                    |
| ----- | ------ | ------------------------------ |
| speed | number | 카메라 이동 속도 (1.0 ~ 10.0). |

-   Return
    -   number: 카메라 이동 애니메이션 적용 속도.
-   Sample
    -   function setEvent 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
var speed = Module.getViewCamera().getAnimationSpeed();
Module.getViewCamera().setAnimationSpeed(5);
```

{% endtab %}
{% endtabs %}

### getDirect(), setDirect(direct) → number

> 카메라의 현재 방향 각도를 설정 및 반환합니다.
>
> 방향각도 값의 범위는 -180도 ~ 180도 사이 입니다.
>
> -   0도: 북쪽
> -   +90도: 동쪽
> -   180도 or -180도: 남쪽
> -   -90도: 서쪽

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| direct | number | 카메라 좌우 회전. |

-   Return
    -   number: 카메라 좌우 회전값 반환 (degree 단위).
-   Sample
    -   function setDirect 참조.
    -   [Sandbox_Camera Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var direct= API.JSCamera.getDirect();
Module.getViewCamera().setDirect(0);
```

{% endtab %}
{% endtabs %}

### getAltitude(), setAltitude(alt) → number

> 카메라 고도를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                         |
| ---- | ------ | ----------------------------------- |
| alt  | number | 카메라 위치 고도 좌표 (meter 단위).     |

-   Return
    -   number: 카메라 위치 고도 좌표 (meter 단위).
-   Sample
    -   function setAltitude 참조.
    -   [Sandbox_Camera Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var altitude = API.JSCamera.getAltitude();
Module.getViewCamera().setAltitude(1000);
```

{% endtab %}
{% endtabs %}

### getFov(), setFov(fov) → number

> 카메라의 화각을 설정 및 반환 합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| ---- | ------ | ------------ |
| fov  | [JSVector2D](../core/jsvector2d.md) | 카메라 화각. |

-   Return
    -   number: 카메라 시야 화각 반환 (degree 단위).
-   Sample
    -   function setFOV 참조.
    -   [Sandbox_Camera Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var FOV= API.JSCamera.getFOV();
Module.getViewCamera().setFov(50);
```

{% endtab %}
{% endtabs %}

### getCenterPoint() → [JSVector3D](../core/jsvector3d.md)

> 화면 중심의 지도 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().getCenterPoint();
```

{% endtab %}
{% endtabs %}

### getLocation() → JSVector3D

> 카메라 위치 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 카메라 위치 좌표 (경도, 위도, 고도)를 성공적으로 반환.
    -   null: 카메라 위치 좌표 반환에 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var location = API.JSCamera.getLocation();
```

{% endtab %}
{% endtabs %}

### getTargetLocation() → [JSVector3D](../core/jsvector3d.md)

> 카메라 타겟 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 카메라 타겟 좌표 (경도, 위도, 고도)를 반환.
    -   카메라 이동 애니메이션이 적용된 상태에서 카메라의 최종 목적지 좌표를 반환.
-   Sample
    -   [Sandbox_Camera Jump](https://sandbox.egiscloud.com/code/main.do?id=camera_jump)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var targetLoc = API.JSCamera.getTargetLocation();
```

{% endtab %}
{% endtabs %}

### setLocation(position) → boolean

> 카메라 위치 좌표를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                          |
| -------- | ----------------------------------- | ------------------------------------ |
| position | [JSVector3D](../core/jsvector3d.md) | 카메라 위치 좌표 (경도, 위도, 고도). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function setMove 참조.
    -   [Sandbox_Camera Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setLocation(new Module.JSVector3D(129.128265, 35.171834, 500.0));
```

{% endtab %}
{% endtabs %}

### getMoveMode(), setMoveMode(type) → boolean

> 1인칭, 3인칭 카메라 회전 모드를 설정 및 반환 합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description       |
| ---- | ------- | ----------------- |
| type | boolean | 카메라 회전 모드. |

-   Return
    -   카메라 모드 반환.
        -   true: 1인칭 시점 회전 모드.
        -   false: 3인칭 시점 회전 모드.
-   Sample
    -   function setPerson 참조.
    -   [Sandbox_Camera Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().getMoveMode();
Module.getViewCamera().setMoveMode(true);
```

{% endtab %}
{% endtabs %}

### setLimitCamera(type)

> 카메라 이동 제한 여부를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description        |
| ---- | ------- | ------------------ |
| type | boolean | 카메라 이동 제한 여부 |

-   Description
    -   카메라 이동 경계 박스 제한과 고도 제한을 설정/해제 합니다.
        - true : 제한 설정
        - false : 제한 해제
-   Sample
    -   [Sandbox_Camera Limit](https://sandbox.egiscloud.com/code/main.do?id=camera_limit)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setLimitCamera(true); // 설정
Module.getViewCamera().setLimitCamera(false); // 해제
```

{% endtab %}
{% endtabs %}

### setLimitRectAlt(minX, minY, maxX, maxY, altitude)

> 카메라 이동 경계 박스를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description                   |
| -------- | ------ | ----------------------------- |
| minX     | number | 경도의 최솟값                   |
| minY     | number | 위도의 최솟값                   |
| maxX     | number | 경도의 최댓값                   |
| maxY     | number | 위도의 최댓값                   |
| altitude | number | 카메라 제한 고도값 (meters 단위) |

-   Description
    -   카메라 이동 경계 박스를 설정합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().setLimitRectAlt(126.920355, 37.520472, 126.930938, 37.529579, 1000);
```
{% endtab %}
{% endtabs %}

### getLimitAltitude(), setLimitAltitude(alt) → number

> 카메라 제한 고도값을 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                       |
| ---- | ------ | --------------------------------- |
| alt  | number | 카메라 제한 고도값 (meters 단위). |

-   Return
    -   number: 카메라 제한 고도값 반환 (meter 단위).
-   Sample
    -   function initPage 참조.
    -   [Sandbox_Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var limitAltitude = API.JSCamera.getLimitAltitude();
Module.getViewCamera().setLimitAltitude(3000);
```

{% endtab %}
{% endtabs %}

### getLimitTilt(), setLimitTilt(tilt) → number

> 카메라 제한 기울기 각도를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                            |
| ---- | ------ | -------------------------------------- |
| tilt | number | 카메라 제한 기울기 각도 (degree 단위). |

-   Return
    -   number: 카메라 제한 기울기 각도를 반환합니다 (degree 단위).
-   Sample
    -   function initPage 참조.
    -   [Sandbox_Camera Path Movement](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var limitTilt = API.JSCamera.getLimitTilt();
API.JSCamera.setLimitTilt(80);
```

{% endtab %}
{% endtabs %}

### getLimitminTilt(), setLimitminTilt(tilt) → number

> 카메라 제한 기울기 최소 각도를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                            |
| ---- | ------ | -------------------------------------- |
| tilt | number | 카메라 제한 기울기 최소 각도 (degree 단위). |

-   Return
    -   number: 카메라 제한 기울기 최소 각도를 반환합니다 (degree 단위).

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setLimitminTilt(20);
var minTilt = API.JSCamera.getLimitminTilt();
```

{% endtab %}
{% endtabs %}

### getLimitmaxTilt(), setLimitmaxTilt(tilt) → number

> 카메라 제한 기울기 최대 각도를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                            |
| ---- | ------ | -------------------------------------- |
| tilt | number | 카메라 제한 기울기 최대 각도 (degree 단위). |

-   Return
    -   number: 카메라 제한 기울기 최대 각도를 반환합니다 (degree 단위).

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setLimitmaxTilt(80);
var maxTilt = API.JSCamera.getLimitmaxTilt();
```

{% endtab %}
{% endtabs %}

### getTilt(), setTilt(tilt) → number

> 카메라 기울기 각도를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                       |
| ---- | ------ | --------------------------------- |
| tilt | number | 카메라 기울기 각도 (degree 단위). |

-   Return
    -   number: 카메라 기울기 각도를 반환합니다 (degree 단위).
-   Sample
    -   See function setTilt.
    -   [Sandbox_Camera Setting](https://sandbox.egiscloud.com/code/main.do?id=camera_set)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var currentTilt = API.JSCamera.getTilt();
Module.getViewCamera().setTilt(80);
```

{% endtab %}
{% endtabs %}

### moveFrontBack(delta)

> 카메라를 현재 시점 방향 기준으로 앞 또는 뒤로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                           |
| ----- | ------ | ------------------------------------- |
| delta | number | 이동 거리. 양수면 앞으로, 음수면 뒤로 이동. |


{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveFrontBack(10.0); // 앞으로 10 이동
API.JSCamera.moveFrontBack(-5.0); // 뒤로 5 이동
```
{% endtab %}
{% endtabs %}

### moveLeftRight(delta)

> 카메라를 현재 시점 기준으로 좌우로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                            |
| ----- | ------ | -------------------------------------- |
| delta | number | 이동 거리. 양수면 오른쪽, 음수면 왼쪽으로 이동. |


{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveLeftRight(10.0); // 오른쪽으로 이동
API.JSCamera.moveLeftRight(-10.0); // 왼쪽으로 이동
```
{% endtab %}
{% endtabs %}

### moveFront()

> 카메라를 현재 시점 방향으로 전진시킵니다.  
> 1인칭(FPS) 모드일 경우 지형 고도에 따라 자동으로 고도를 조정합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   기본 이동 거리(delta)는 내부 설정값(`getMoveDelta`)을 따릅니다.  
    -   FPS 모드 활성화 시, 이동 후 지형 높이에 맞춰 카메라 고도가 자동 보정됩니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveFront();
```
{% endtab %}
{% endtabs %}

### moveBack()

> 카메라를 뒤로 이동합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라를 뒤로 이동합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveBack();
```

{% endtab %}
{% endtabs %}

### moveLeft()

> 카메라를 현재 위치에서 왼쪽으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라를 좌측 방향으로 이동합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveLeft();
```

{% endtab %}
{% endtabs %}

### moveRight()

> 카메라를 현재 시점 기준으로 오른쪽으로 이동합니다.  

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라를 오른쪽으로 이동합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveRight();
```

{% endtab %}
{% endtabs %}

### rotateUp()

> 카메라를 위쪽으로 회전합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라의 X축 기준 기울기(틸트)를 감소시켜 위로 올립니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.rotateUp();
```

{% endtab %}
{% endtabs %}

### rotateDown()

> 카메라를 아래쪽으로 회전합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라의 X축 기준 기울기(틸트)를 증가시켜 아래로 내립니다. 

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.rotateDown();
```

{% endtab %}
{% endtabs %}

### moveUp()

> 카메라를 현재 위치에서 위로 이동합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라를 현재 위치에서 위로 이동합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveUp();
```

{% endtab %}
{% endtabs %}

### moveDown()

> 카메라를 현재 위치에서 아래로 이동합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라를 시점 기준 아래로 이동합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.moveDown();
```

{% endtab %}
{% endtabs %}

### getCameraSpeed(), setCameraSpeed(speed) → number

> 카메라의 이동 속도를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description         |
| ----- | ------ | ------------------- |
| speed | number | 카메라 이동 속도(정수) |

{% endtab %}
{% tab title="Template" %}

``` javascript
var API = {
    JSCamera : Module.getViewCamera();
};
var speed = API.JSCamera.getCameraSpeed();
Module.getViewCamera().setCameraSpeed(5);
```

{% endtab %}
{% endtabs %}

### setTraceTarget(target) → boolean

> 카메라의 추적 대상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type             | Description               |
| ------ | ---------------- | ------------------------- |
| target | JSTraceTarget    | 추적 대상 객체입니다.        |

-   Return  
    -   `true`: 추적 대상 설정 성공  
    -   `false`: 대상이 유효하지 않거나 설정 실패

-   Description  
    -   지정된 객체를 카메라가 지속적으로 따라가도록 설정합니다.  

{% endtab %}
{% tab title="Template" %}

```javascript
var traceTarget = Module.createTraceTarget(model.getId());
traceTarget.set({
    object: model,
    tilt: 45.0,
    direction: 0.0,
    distance: 100.0,
});

var camera = Module.getViewCamera();
camera.setTraceTarget(traceTarget);
```

{% endtab %}
{% endtabs %}

### setTraceActive(active) → boolean

> 추적 대상의 추적 활성화 여부를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type    | Description                       |
| ------ | ------- | --------------------------------- |
| active | boolean | `true`: 추적 활성화, `false`: 비활성화 |

-   Return  
    -   `true`: 설정 성공  
    -   `false`: 설정 실패 (내부 엔진 미정의 상태 등)

-   Description  
    -   `setTraceTarget()`으로 설정한 대상에 대해 추적을 켜거나 끌 수 있습니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setTraceActive(true);  // 추적 시작
API.JSCamera.setTraceActive(false); // 추적 중단
```

{% endtab %}
{% endtabs %}

### ReleaseTrace() → boolean

> 카메라의 추적 대상을 삭제합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   설정된 카메라의 추적 대상을 삭제합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.ReleaseTrace();
```

{% endtab %}
{% endtabs %}

### bankLeft()

> 카메라를 왼쪽으로 기울입니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라의 롤(Roll) 축을 따라 왼쪽으로 회전(기울기)합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.bankLeft();
```

{% endtab %}
{% endtabs %}

### bankRight()

> 카메라를 오른쪽으로 기울입니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라의 롤(Roll) 축을 따라 오른쪽으로 회전(기울기)합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.bankRight();
```

{% endtab %}
{% endtabs %}

### setPlayerMode(mode) → void

> 1인칭 카메라 모드에서 플레이어 모드(물리 기반)를 활성화/비활성화 합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    | Description                                           |
| ----- | ------- | ----------------------------------------------------- |
| mode  | boolean | <p>플레이어 모드<br>true: 활성화<br>false: 비활성화</p>      |

-   Description  
    -   [1인칭 지형 결합 모드](#setunionmode-mode-void)와 함께 활성화 되어 있을 때, [점프](#jump-void)가 가능하며 자연스러운 중력 낙하 효과가 적용됩니다.

-   Sample  
    -   [Sandbox_View Mode](https://sandbox.egiscloud.com/code/main.do?id=camera_view_mode)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setPlayerMode(true); // 플레이어 모드 활성화
API.JSCamera.setPlayerMode(false); // 플레이어 모드 비활성화
```

{% endtab %}
{% endtabs %}

### isGround() → boolean

> 1인칭 카메라 모드에서 카메라가 현재 지면에 닿아 있는지 여부를 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Description
    -   [플레이어 모드](#setplayermode-mode-void)가 활성화된 상태에서만 지면 여부를 판별합니다.
    -   true일 때만 [점프](#jump-void)가 가능합니다.

-   Return  
    -   true : 지면에 닿아 있음.
    -   false : 지면과 닿아 있지 않음 또는 [플레이어 모드]((#setplayermode-mode-void))가 비활성화

-   Sample
    -   [Sandbox_Camera Jump](https://sandbox.egiscloud.com/code/main.do?id=camera_jump)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.isGround();
```

{% endtab %}
{% endtabs %}

### jump() → void

> 1인칭 카메라 지형결합 모드, 플레이어 모드에서 카메라가 자연스럽게 공중으로 올라갔다가 떨어집니다.

{% tabs %}
{% tab title="Information" %}

- Description
    -   [1인칭 지형 결합 모드](#setunionmode-mode-void)와 [플레이어 모드](#setplayermode-mode-void)가 모두 활성화된 상태에서만 동작합니다.
    -   [점프 세기](#getjumpforce-setjumpforce-jumpforce-number), [중력](#getgravity-setgravity-gravity-number), [시간 간격](#gettimestep-settimestep-timestep-number)을 조절할 수 있습니다.

-   Sample
    -   [Sandbox_Camera Jump](https://sandbox.egiscloud.com/code/main.do?id=camera_jump)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setUnionMode(true);
API.JSCamera.setPlayerMode(true);
API.JSCamera.jump();
```

{% endtab %}
{% endtabs %}

### getJumpForce(), setJumpForce(jumpForce) → number

> 초기 점프 속도(점프 세기)를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description            |
| --------- | ------ | ---------------------- |
| jumpForce | number | 초기 점프 속도(점프 세기) |

-   Sample
    -   [Sandbox_Camera Jump](https://sandbox.egiscloud.com/code/main.do?id=camera_jump)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setJumpForce(30.0); // 기본값 10.0
var jumpForce = API.JSCamera.getJumpForce();
```

{% endtab %}
{% endtabs %}

### getGravity(), setGravity(gravity) → number

> 카메라 중력을 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description |
| ------- | ------ | ----------- |
| gravity | number | 카메라 중력   |

-   Sample
    -   [Sandbox_Camera Jump](https://sandbox.egiscloud.com/code/main.do?id=camera_jump)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setGravity(1.62); // 기본값 9.8
var gravity = API.JSCamera.getGravity();
```

{% endtab %}
{% endtabs %}

### getTimeStep(), setTimeStep(timeStep) → number

> 카메라 점프/낙하 동작의 시간 간격을 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description      |
| -------- | ------ | ---------------- |
| timeStep | number | 점프/낙하 시간 간격 |

-   Description
    -   한 프레임 당 점프/낙하 동작의 간격을 설정합니다.
    -   timeStep이 작을 수록 구간을 더 촘촘하게 잘라 점프/낙하 속도가 느려집니다.

-   Sample
    -   [Sandbox_Camera Jump](https://sandbox.egiscloud.com/code/main.do?id=camera_jump)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setTimeStep(0.08); // 기본값 0.05
var timeStep = API.JSCamera.getTimeStep();
```

{% endtab %}
{% endtabs %}

### setLandingElevation(elevation) → void

> [플레이어 모드](#setplayermode-mode-void)에서 카메라의 착지 고도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description      |
| --------- | ------ | ---------------- |
| elevation | number | 카메라의 착지 고도 |

-   Description  
    -   카메라가 [플레이어 모드](#setplayermode-mode-void)인 경우에만 실행됩니다.
    -   점프/낙하 시 카메라는 설정한 고도에 착지합니다.

-   Sample
    -   [Sandbox_View Mode](https://sandbox.egiscloud.com/code/main.do?id=camera_view_mode)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setLandingElevation(20.0);
```

{% endtab %}
{% endtabs %}

### setLandingElevationToTerrain() → void

> [플레이어 모드](#setplayermode-mode-void)에서 카메라의 착지 고도를 현재 지형 고도로 설정합니다.

{% tabs %}
{% tab title="Information" %}

-   Description  
    -   카메라가 [플레이어 모드](#setplayermode-mode-void)인 경우에만 실행됩니다.
    -   점프/낙하 시 카메라는 설정한 시점의 지형 고도에 착지합니다.

-   Sample
    -   [Sandbox_View Mode](https://sandbox.egiscloud.com/code/main.do?id=camera_view_mode)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setLandingElevationToTerrain();
```

{% endtab %}
{% endtabs %}

### setUnionMode(mode) → void

> 1인칭 카메라 모드에서 지형 결합을 실행합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    | Description                                           |
| ----- | ------- | ----------------------------------------------------- |
| mode  | boolean | <p>카메라 지형 결합<br>true: 실행<br>false: 해제</p>      |

-   Description  
    -   카메라가 1인칭 모드인 경우에만 실행됩니다.

-   Sample  
    -   [Sandbox_View Mode](https://sandbox.egiscloud.com/code/main.do?id=camera_view_mode)

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};
API.JSCamera.setUnionMode(true); // 실행
API.JSCamera.setUnionMode(false); // 해제
```

{% endtab %}
{% endtabs %}

### setAutoMovePath(pathList) → boolean

> 카메라 자동 이동 경로를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type         | Description                          |
| --------- | ------------ | ------------------------------------ |
| pathList  | Array<Object> | 이동 경로를 구성하는 지점 목록입니다. 각 요소는 `{ position, direction, tilt }` 객체로 구성됩니다. |

-   Description  
    -   최소 2개 이상의 경로 지점을 포함해야 합니다.  
    -   각 경로 지점에는 `position`(JSVector3D), `direction`(number), `tilt`(number)가 포함됩니다.  
    -   입력값이 유효하지 않으면 경로는 등록되지 않습니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};

var pathList = [
    { position: new Module.JSVector3D(129.128265, 35.171834, 500), direction: 0.0, tilt: 80.0 },
    { position: new Module.JSVector3D(129.128500, 35.172000, 500), direction: 20.0, tilt: 85.0 }
];

API.JSCamera.setAutoMovePath(pathList);
```

{% endtab %}
{% endtabs %}

### setLockOrientationAutoMove(type) → void

> 카메라 방향/틸트 고정 여부를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                          |
| ---- | ------- | ------------------------------------ |
| type | boolean | 카메라 방향/틸트 고정 여부 설정 (true: 고정, false: 고정 해제) |

-   Description
    -   카메라 방향과 틸트의 고정 여부를 설정합니다.
    -   기본값은 true 입니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera();
};

API.JSCamera.setLockOrientationAutoMove(true); // 고정
API.JSCamera.setLockOrientationAutoMove(false); // 고정 해제
```

{% endtab %}
{% endtabs %}

### clearAutoMovePosition() → boolean

> 설정된 카메라 자동 이동 좌표 목록을 삭제합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true : 삭제 성공.
    -   false : 삭제 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getViewCamera().clearAutoMovePosition();
```

{% endtab %}
{% endtabs %}

### AltitudeUp()

> 카메라의 고도를 높입니다.  
> 내부적으로는 현재 시점을 기준으로 일정한 틸트, 방향값을 유지하면서, 고도를 증가시켜 새로운 위치로 카메라를 이동시킵니다.

{% tabs %}
{% tab title="Information" %}

| 항목 | 설명 |
|------|------|
| 클래스 | `JSCamera` |
| 반환값 | 없음 |
| 파라미터 | 없음 |
| 설명 | 현재 카메라의 위치에서 고도를 증가시킨 위치로 카메라를 이동시킵니다. 시점(lookAt)은 그대로 유지하며, 틸트와 방향(heading)도 유지됩니다. 고도 증가는 내부 정의된 일정한 거리만큼 수행됩니다. |
| 관련 API | `moveLookAt`, `SetCamera`, `SetHeading` |

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera()
};
API.JSCamera.AltitudeUp();
```
{% endtab %}
{% endtabs %}

### moveLookAt(lookAt, tilt, direct, distance) → void

> 특정 지점을 기준으로 카메라를 이동시킵니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type       | Description |
|----------|------------|-------------|
| lookAt   | JSVector3D | 카메라가 바라볼 대상의 위치. 위도(Y), 경도(X), 고도(Z) 값으로 구성됩니다. |
| tilt     | number     | 카메라의 상하 기울기 각도 (단위: 도, degree) |
| direct   | number     | 카메라의 방위각, 즉 수평 방향 (단위: 도, degree) |
| distance | number     | `lookAt` 지점으로부터 카메라까지의 거리 (단위: meter) |

- Return  
  - 없음 (void)

- Description  
  - 지정한 위치를 중심으로, 입력받은 틸트와 방향, 거리 값을 기반으로 카메라의 시점을 설정합니다.
  - 내부적으로 구면 좌표계를 사용하여 카메라 위치를 계산하고, `SetCamera()` 및 `SetHeading()`을 호출하여 반영합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera()
};

var lookAt = new Module.JSVector3D();
lookAt.X = 126.9780; // 경도
lookAt.Y = 37.5665;  // 위도
lookAt.Z = 300.0;    // 고도 (meter)

API.JSCamera.moveLookAt(lookAt, 45.0, 90.0, 1000.0);
```
{% endtab %}
{% endtabs %}

### setViewAt(longitude, latitude, altitude, tilt, direct) → void

> 특정 지점을 바라보도록 카메라를 설정합니다.
>
> 입력 변수값(altitude, tilt, heading)을 적용하여 카메라를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type       | Description                                 |
|-----------|------------|---------------------------------------------|
| longitude | number     | 카메라가 바라볼 위치의 경도 좌표 (degrees 단위). |
| latitude  | number     | 카메라가 바라볼 위치의 위도 좌표 (degrees 단위)  |
| altitude  | number     | 카메라 위치 고도 좌표 (meter 단위).             |
| tilt      | number     | 카메라의 상하 기울기 각도 (단위: 도, degree).    |
| direct    | number     | 카메라의 방위각, 즉 수평 방향 (단위: 도, degree) |

- Return  
  - 없음 (void)

- Description  
  - 지정한 위치를 중심으로, 입력받은 고도값과 틸트, 방향을 기반으로 카메라의 시점을 설정합니다.  
  - 바라보는 지점의 고도는 0이며, `SetCamera()` 및 `SetHeading()`을 호출하여 반영합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera()
};

var longitude = 126.9780; // 경도
var latitude = 37.5665;  // 위도
API.JSCamera.setViewAt(longitude, latitude, 1000, 45, 90);
```
{% endtab %}
{% endtabs %}

### setViewMode(vMode) → void

> 카메라의 뷰 모드를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type  | Description |
|--------|-------|-------------|
| vMode  | int   | 뷰 모드 타입. 정수값으로 지정되며, 엔진 내부에서 정의된 시점 모드로 전환됩니다. |

- Return  
  - 없음 (void)

- Description  
  - 카메라의 뷰 모드를 설정합니다.  
  - `vMode`는 엔진 내부에 정의된 값으로, 예를 들어 기본 뷰, 3인칭 추적 뷰, 탑다운 뷰 등으로 전환될 수 있습니다.  
  - 설정 후 `UpdateFrame()`을 호출하여 프레임 갱신을 즉시 반영합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSCamera : Module.getViewCamera()
};

// 예: 0 = 기본 뷰, 1 = 3인칭 뷰 등 (정의는 엔진에 따라 다름)
API.JSCamera.setViewMode(1);
```
{% endtab %}
{% endtabs %}

### Type Definitions

#### JSCamera.MoveBoundaryOption

> Options for moving the camera based on area information.

| Name     | Type                                           | Description            |
| -------- | ---------------------------------------------- | ---------------------- |
| boundary | [Rect2D](../etc/tag-list.md#rect2d-style-type) | 카메라 이동 경계 박스. |
| complete | function                                       | 이동 완료 콜백 함수.   |
