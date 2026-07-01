---
description: 지도 내 고스트 심볼 객체 생성를 생성 및 설정하기 위한 API 입니다.
---

# JSGhostSymbol

> Module.createGhostSymbol() API를 생성합니다.

```javascript
var object = Module.createGhostSymbol("ID");
```
## Properties

| Name     			| Type                                	| Description                   |
| ----------------- | ------------------------------------- | ----------------------------- |
| opacity 			| number                             	| 객체 투명값 (0.0 ~ 1.0).		|
| color      		| [JSColor](../core/jscolor.md)        	| 객체 색상값.                   	|
| lightColor     	| [JSColor](../core/jscolor.md)        	| 객체 조명 색상값.              	|
| zBufferOff     	| boolean                              	| depthBuffer 사용 유무.        	|

## Function

### getBasePointX() → number

> 고스트 심볼 중심 좌표를 기준으로 X축으로 이동 값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: X축 이동 값(미터).
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getBasePointY() → number

> 고스트 심볼 중심 좌표를 기준으로 Y축으로 이동 값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: Y축 이동 값(미터).
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getBasePointZ() → number

> 고스트 심볼 중심 좌표를 기준으로 Z축으로 이동 값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: Z축 이동 값(미터).
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getGhostSymbolMapKey() → string

> 고스트 심볼의 참조된 객체 명칭을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   string: 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getId() → string

> 오브젝트의 Key를 반환.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   string : 오브젝트 Key 문자열 반환 성공.
    -   null : 오브젝트가 null일 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var strKey = object.getId();
```

{% endtab %}
{% endtabs %}

### getPosition() → [JSVector3D](../core/jsvector3d.md)

> 고스트 심볼 객체의 중심 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return

    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.
    -   null: 반환 실패.

-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```
                                                                                                        
{% endtab %}
{% endtabs %}

### getHeight() → number

> 고스트 심볼 객체의 높이를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return

    -   number: 반환 성공.
    -   0.0: 반환 실패.(렌더링 유효 오브젝트 아님)

{% endtab %}
{% tab title="Template" %}

```javascript
var height = object.getHeight();
```

{% endtab %}
{% endtabs %}

### getRotationX() → number

> 고스트 심볼 객체의 X축 회전 값(degree 단위)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: X축 회전 값.
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getRotationY() → number

> 고스트 심볼 객체의 Y축 회전 값(degree 단위)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: Y축 회전 값.
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getRotationZ() → number

> 고스트 심볼 객체의 Z축 회전 값(degree 단위)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: Z축 회전 값.
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getScale() → [JSSize3D](../core/jssize3d.md)

> 고스트 심볼 객체의 크기 비율을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSSize3D](../core/jssize3d.md): 반환 성공(x,y,z).
    -   null: 반환 실패.
-   Sample
    -   function displayGhostSymbolProperties 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### moveVertically(alt) → boolean

> 객체를 수직(위/아래) 방향으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description          |
| ---- | ------ | -------------------- |
| alt  | number | 이동 값(meter 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var newGhostSymbol = Module.createGhostSymbol("newGhostSymbol");
newGhostSymbol.moveVertically(150.0);
```

{% endtab %}
{% endtabs %}

### setBasePoint(x, y, z) → boolean

> 고스트 심볼 객체의 중심 좌표를 기준으로 입력 변수값(x, y, z) 만큼 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description              |
| ---- | ------ | ------------------------ |
| x    | number | X축 이동 값(meter 단위). |
| y    | number | Y축 이동 값(meter 단위). |
| z    | number | Z축 이동 값(meter 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function setBasePoint 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setGhostSymbol(name) → boolean

> 고스트 심볼을 관리하는 목록에서 입력 변수값(name)에 해당되는 고스트 심볼을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| name | string | 객체 고유 명칭. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createGhostSymbol 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setPosition(position) → boolean

> 고스트 심볼 객체의 위치를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                  |
| -------- | ----------------------------------- | ---------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 위치 좌표(경도, 위도, 고도). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createGhostSymbol 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript
var newGhostSymbol = Module.createGhostSymbol("newGhostSymbol");

// 오브젝트 위치 지정
var vPosition = new Module.JSVector3D(129.126046, 35.169985, 4.5);
newGhostSymbol.setPosition(vPosition);	
```

{% endtab %}
{% endtabs %}

### setScale(scale) → boolean

> 고스트 심볼 객체의 크기 비율을 설정합니다.
>
> 입력 변수값(scale)을 구성 요소는 0보다 큰값이 설정되어야합니다.
>
> 초기 설정값은 (1,1,1) 입니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                            | Description               |
| ----- | ------------------------------- | ------------------------- |
| scale | [JSSize3D](../core/jssize3d.md) | 크기 비율(X축, Y축, Z축). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createGhostSymbol 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript
var newGhostSymbol = Module.createGhostSymbol("newGhostSymbol");

// 오브젝트 스케일 지정
var vScale = new Module.JSSize3D(1.0, 1.5, 1.0);
newGhostSymbol.setScale(vScale);
```

{% endtab %}
{% endtabs %}

### setRotation(x, y, z) → boolean

> 고스트 심볼 객체의 회전 값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description               |
| ---- | ------ | ------------------------- |
| x    | number | X축 회전 값(degree 단위). |
| y    | number | Y축 회전 값(degree 단위). |
| z    | number | Z축 회전 값(degree 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function setRotation 참조.
    -   [Sandbox_Ghost Symbol Editing](https://sandbox.egiscloud.com/code/main.do?id=object_ghost_symbol_edit)

{% endtab %}
{% tab title="Template" %}

```javascript
var newGhostSymbol = Module.createGhostSymbol("newGhostSymbol");
newGhostSymbol.setRotation(45.0, 90.0, 180.0);
```

{% endtab %}
{% endtabs %}

### setDirection(angle) → boolean

> 고스트 심볼 객체의 방향 각도를 설정합니다.
>
> [setRotation(0, angle, 0)](#setrotationx-y-z--boolean)과 같은 기능을 수행합니다.


{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description              |
| ----- | ------ | ------------------------ |
| angle | number | 오브젝트 방향(degree 단위). |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var newGhostSymbol = Module.createGhostSymbol("newGhostSymbol");
newGhostSymbol.setDirection(90.0);
```

{% endtab %}
{% endtabs %}

### getDirection() → number

> 고스트 심볼 객체의 방향 각도를 반환합니다.
>
> [getRotationY()](#getrotationy--number)와 같은 기능을 수행합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 오브젝트 방향(degree 단위).

{% endtab %}
{% tab title="Template" %}

```javascript
var newGhostSymbol = Module.createGhostSymbol("newGhostSymbol");
var direction = newGhostSymbol.getDirection();
```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getColor(), setColor(color) → [JSColor](../core/jscolor.md)

> 고스트 심볼 객체의 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| color | [JSColor](../core/jscolor.md) | 색상값.     |

-   Return
    -   객체 색상.

{% endtab %}
{% tab title="Template" %}

```javascript

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
    -   string: 객체 이름을 성공적을 반환.
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

### getOpacity(), setOpacity(opacity) → number

> 고스트 심볼 객체 투명도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description |
| ------- | ------ | ----------- |
| opacity | number | 투명도(0.0 ~ 1.0).     |

-   Return
    -   number: 객체에 설정된 투명도를 성공적으로 반환.

{% endtab %}
{% tab title="Template" %}

```javascript

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

### setScreenFixedSize(size) → boolean

> 고스트 심볼 객체의 화면 고정 크기를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                                 |
| ---- | ------- | --------------------------------------------------------------------------- |
| size | number  | 고정 크기 값(px 단위). `null` 입력 시 화면 고정 크기 모드가 해제됩니다. |

-   Return  
    -   true: 설정 성공.  
    -   false: 잘못된 입력 값 등으로 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
// 화면 고정 크기 24픽셀로 설정
object.setScreenFixedSize(24.0);

// 화면 고정 크기 해제
object.setScreenFixedSize(null);
```

{% endtab %}
{% endtabs %}
