---
description: 지도 내 선 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSLineString

> Module.createLineString() API를 생성합니다.

```javascript
var object = Module.createLineString("ID");
```

## Function

### createbyJson(option) → string

> 선 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                                    | Description |
| ------ | ----------------------------------------------------------------------- | ----------- |
| option | [JSLineString.CreateOptions](#jslinestringcreateoptions) | 속성 정보.  |

-   Return
    -   "success": 생성 성공.
    -   이 외 오류 원인을 포함한 에러 메시지
-   Sample
    -   function createLine 참조.
    -   [Sandbox_Line](https://sandbox.egiscloud.com/code/main.do?id=object_line_Json)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getBoundary() → [JSAABBox3D](../core/jsaabbox3d.md)

> 선 객체를 포함하는 박스 영역을 반환합니다.

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

> 선 객체를 중심 좌표(경도, 위도, 고도)를 반환합니다.

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

### getExtent() → number

> 선 객체를 포함하는 박스 영역을 min, max간 거리를 반환합니다..

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 거리 반환.

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

### getLength(terrain) → number

> 선 객체의 총 길이를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                                                                                  |
| ------- | ------- | ------------------------------------------------------------------------------------------------------------ |
| terrain | boolean | <p>지형 곡면률 설정 유무.<br>true: 지형 곡면률 고려한 길이 계산.<br>false: 입력된 좌표에 대한 길이 계산.</p> |

-   Return
    -   number(0 이상): 반환 성공.
    -   number(-1.0): 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var length = object.getLength();
```

{% endtab %}
{% endtabs %}

### SetDashType(dash) → boolean

> 선 간격을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| dash | number | 점선 간격.  |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPartCoordinates(coordinates, parts)

> 선 객체를 생성합니다.
>
> 입력 변수값(coordinates)은 3개 이상 입력되어야 합니다.
>
> 입력 변수값(parts)은 1개 이상 입력되어야 합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                            |
| ----------- | ------------------------------------- | -------------------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 좌표 목록(경도, 위도, 고도).           |
| parts       | [Collection](../core/collection.md)   | 직선을 구성하는 coordinates 개수 목록. |

-   Sample
    -   function createBufferPolygon 참조.
    -   [Sandbox_Line Buffering](https://sandbox.egiscloud.com/code/main.do?id=object_line_buffering)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setUnionMode(type), getUnionMode() → boolean

> 선 객체 가시화 옵션을 설정 및 반환합니다.
>
> 선 생성 시 지형 결합 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                |
| ---- | ------- | ---------------------------------------------------------- |
| type | boolean | <p>true: 지형 결합 가시화(RTT).<br>false: 일반 가시화.</p> |

-   Sample
    -   function createObjectToPathPosition 참조.
    -   [Sandbox_Path Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_line_path_distance)

{% endtab %}
{% tab title="Template" %}

```javascript
let line = Module.createLineString(id);
/* line 좌표 설정 */
line.setUnionMode(true);
```

{% endtab %}
{% endtabs %}

### setLineType(type)

> 선의 타입을 설정합니다.
>
> 실선, 점선 등과 같은 타입을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                                                |
| ---- | ------ | ---------------------------------------------------------- |
| type | number | <p>0: NORMAL<br>1: OUTLINE<br>2: GLOW<br>3: ARROW<br>4: DASH<br>5: FIRE<br>6: TWINKLE<br>7: WARNING</p> |

-   Sample
    -   타입 별 가시화 샘플
    -   [Sandbox_Line](https://sandbox.egiscloud.com/code/main.do?id=object_line_Json)
    -   [Sandbox_Line Effect](https://sandbox.egiscloud.com/code/main.do?id=object_line_effect)

{% endtab %}
{% tab title="Template" %}

```javascript
let line = Module.createLineString(id);
/* line 좌표 설정 */
line.setLineType(2); // GLOW
```

{% endtab %}
{% endtabs %}

### setDepthBufferTest(type)

> 선의 Depth 버퍼를 활성화/비활성화 합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description              |
| ---- | ------- | ------------------------ |
| type | boolean | <p>true: 활성화<br>false: 비활성화</p> |


{% endtab %}
{% tab title="Template" %}

```javascript
line.setDepthBufferTest(true); // 활성화
line.setDepthbufferTest(false); // 비활성화
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

### getCoordinates(), setCoordinates(coordinates) → [Collection](../core/collection.md)

> 선 객체를 구성하는 좌표 목록을 설정합니다.
>
> 입력 변수값(coordinates)은 3개 이상 입력되어야 합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                | Description                  |
| ----------- | ----------------------------------- | ---------------------------- |
| coordinates | [Collection](../core/collection.md) | 좌표 목록(경도, 위도, 고도). |

-   Return
    -   [Collection](../core/collection.md): 선을 구성하는 좌표 목록.
-   Sample
    -   function createPathLine 참조.
    -   [Sandbox_Path Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_line_path_distance)

{% endtab %}
{% tab title="Template" %}

```javascript
var coorList = object.getCoordinates();
```

{% endtab %}
{% endtabs %}

### getStyle(), setStyle(style) → [JSPolyLineStyle](jspolylinestyle.md)

> 선 객체를 [JSPolyLineStyle](jspolylinestyle.md)으로 설정된 스타일로 설정합니다.
>
> 색상, 두께, 투명도 등을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                  | Description |
| ----- | ------------------------------------- | ----------- |
| style | [JSPolyLineStyle](jspolylinestyle.md) | 선 스타일.  |

-   Return
    -   [JSPolyLineStyle](jspolylinestyle.md): 설정 성공.
-   Sample
    -   function createBufferPolygon 참조.
    -   [Sandbox_Line Buffering](https://sandbox.egiscloud.com/code/main.do?id=object_line_buffering)

{% endtab %}
{% tab title="Template" %}

```javascript
var objectStyle = polyLine.getStyle();
```

{% endtab %}
{% endtabs %}

### Type Definitions

#### JSLineString.CreateOptions

> 직선 객체 생성 옵션.

| Name        | Type                                                    | Attributes | Default                     | Description                                                |
| ----------- | ------------------------------------------------------- | ---------- | --------------------------- | ---------------------------------------------------------- |
| coordinates | [coordinates Type](../etc/tag-list.md#coordinates-type) |            |                             | 좌표 목록 옵션.                                            |
| type        | number                                                  | optional   | 0                           | 라인 가시화 타입.                                          |
| skip        | number                                                  | optional   | 1                           | 애니메이션 디테일 옵션.                                    |
| width       | number                                                  | optional   | 1                           | 라인 굵기 옵션.                                            |
| dash        | number                                                  | optional   | 0                           | 점선 간격 옵션.                                            |
| speed       | number                                                  | optional   | 0                           | 애니메이션 속도 옵션.                                      |
| union       | boolean                                                 | optional   | false                       | <p>true: 지형 결합 가시화(RTT).<br>false: 일반 가시화.</p> |
| depth       | boolean                                                 | optional   | true                        | <p>true: 일반 가시화.<br>false: 깊이감 미표현 가시화.</p>  |
| color       | [JSColor](../core/jscolor.md)                           | optional   | JSColor(200, 255, 255, 255) | 라인 가시화 색상.                                          |
