---
description: 지도 내 지형의 터파기 분석 기능 설정을 위한 API입니다.
---

# JSTransparency

> Module.getTransparency API를 생성합니다.

```javascript
var transparency = Module.getTransparency();
```

## Function

### clear()

> 터파기 결과를 초기화 합니다.

{% tabs %}
{% tab title="Template" %}

```javascript
Module.getTransparency().clear();
```

{% endtab %}
{% endtabs %}

### create(coordinates) → number

> 입력 좌표를 받아 터파기 객체를 생성합니다.
>
> 입력 변수값(coordinates)은 ([JSVector3D](../core/jsvector3d.md), [JSVector3D](../core/jsvector3d.md), ...) 영역 좌표 목록으로 구성됩니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description              |
| :---------- | :------------------------------------ | :----------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 터파기 영역 좌표 리스트. |

-   Return
    -   number > 0: 생성 성공.
    -   -1: 생성 실패.
-   Sample
    -   function createTransparency 참조.
    -   [Sandbox_Creating Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_create)

{% endtab %}
{% tab title="Template" %}

```javascript
var AreaVertices = Module.getMap().getInputPoints();
var nIndex = Module.getTransparency().create(AreaVertices);
```

{% endtab %}
{% endtabs %}

### setAutoMove(coordinates, frame) → boolean

> 입력된 경로로 이동하는 원형 터파기의 경로와 속도를 설정합니다.
>
> 입력 변수값(coordinates)은 ([JSVector2D](../core/jsvector3d.md), [JSVector2D](../core/jsvector3d.md), ...) 이동 좌표 목록으로 구성됩니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                       |
| :---------- | :------------------------------------ | :-------------------------------- |
| coordinates | [JSVec2Array](../core/jsvec2array.md) | 터파기 객체 이동 좌표 목록.       |
| frame       | number                                | 터파기 애니메이션 갱신 프레임 수. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function setTransparencyAutoMove 참조.
    -   [Sandbox_Moving Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_move)

{% endtab %}
{% tab title="Template" %}

```javascript
var movePositionList = new Module.JSVec2Array();
movePositionList.push(new Module.JSVector2D(127.03691229708741, 37.509635136930626));
movePositionList.push(new Module.JSVector2D(127.03987097629198, 37.50932526196098));
movePositionList.push(new Module.JSVector2D(127.03695802409491, 37.50865005215346));
movePositionList.push(new Module.JSVector2D(127.03985503640686, 37.50816724210336));
movePositionList.push(new Module.JSVector2D(127.03711645791172, 37.50779863443866));
movePositionList.push(new Module.JSVector2D(127.03978095384555, 37.50738212410067));
// Set auto-move for excavation
Module.getTransparency().setAutoMove(movePositionList, 5);
```

{% endtab %}
{% endtabs %}

### setDepth(depth)

> 터파기 높이를 설정합니다.
>
> 높이는 지상 기준이 아닌 지하 기준입니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                     |
| :---- | :----- | :------------------------------ |
| depth | number | 터파기 높이 설정 (meters 단위). |

-   Sample
    -   function createTransparency 참조.
    -   [Sandbox_Setting Excavation Depth](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_depth)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getTransparency().setDepth(5.5);
```

{% endtab %}
{% endtabs %}

### setRadius(radius)

> 원형 터파기 반경을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description                |
| :----- | :----- | :------------------------- |
| radius | number | 터파기 반경 (meters 단위). |

-   Sample
    -   function setTransparencyRadius 참조.
    -   [Sandbox_Setting Excavation Radius](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_radius)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getTransparency().setRadius(500.0);
```

{% endtab %}
{% endtabs %}

### setTexture(data, width, height, type) → boolean

> 터파기 구성하는 면에 이미지를 설정합니다.
>
> data 변수는 Uint8Array 기반의 바이너리 배열 데이터.

{% tabs %}
{% tab title="Information" %}

| Name   | Type    | Description                                                      |
| :----- | :------ | :--------------------------------------------------------------- |
| data   | object  | 이미지 데이터.                                                   |
| width  | number  | 이미지 너비.                                                     |
| height | number  | 이미지 높이.                                                     |
| type   | boolean | <p>true: 터파기 측면에 적용.<br>false: 터파기 바닥면에 적용.</p> |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function setTransparencyTexture 참조.
    -   [Sandbox_Excavation Texture](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_texture)

{% endtab %}
{% tab title="Template" %}

```javascript
var img = new Image();
// Load texture image
img.onload = function () {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);
    var imageSize = new Module.JSSize2D(img.width, img.height);
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    // Set excavation texture
    var transparency = Module.getTransparency();
    transparency.setTexture(imageData, canvas.width, canvas.height, true); // floor texture
    transparency.setTexture(imageData, canvas.width, canvas.height, false); // wall texture
};
img.src = "./image/FaceImage.jpg";
```

{% endtab %}
{% endtabs %}

### startAutoMove() → boolean

> 등록된 경로로 터파기 자동 이동을 실행합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 동작 성공.
    -   false: 동작 실패.
-   Sample
    -   function startTransparencyAutoMove 참조.
    -   [Sandbox_Moving Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_move)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getTransparency().startAutoMove();
```

{% endtab %}
{% endtabs %}

### stopAutoMove()

> 자동 이동 중인 터피가 경로 애니메이션을 종료합니다.

{% tabs %}
{% tab title="Information" %}

-   Sample
    -   function stopTransparencyAutoMove 참조.
    -   [Sandbox_Moving Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_move)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getTransparency().stopAutoMove();
```

{% endtab %}
{% endtabs %}
