---
description: 지도 내 각종 이벤트 관련 기능을 설정 및 제어하기 위한 API 입니다.
---

# JSControl

> Module.getControl() API를 생성합니다.

```javascript
var object = Module.getControl();
```

## Properties

| Name     				| Type                                	| Description                   |
| --------------------- | ------------------------------------- | ----------------------------- |
| keyboard_sensitivity  | number                              	| 키보드 이동 민감도              |


## Function

### activeMouse(type) → boolean

> 마우스 콜백 이벤트를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                      |
| :--- | :------ | :--------------------------------------------------------------- |
| type | boolean | <p>true: 콜백 이벤트 활성화.<br>false: 골백 이벤트 비활성화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setMouseWheelCenterMode(type)

> 마우스 휠을 통한 지도 확대 축소 시 마우스 위치 기준 또는 화면 중심 기준으로 동작 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                    |
| :--- | :------ | :------------------------------------------------------------- |
| type | boolean | <p>true: 화면 중심으로 설정.<br>false: 마우스 위치로 설정.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getKeyControlEnable(), setKeyControlEnable(type) → boolean

> 키보드를 통한 카메라 조작 가능 유무를 설정합니다.
>
> 키보드 기본 입력키에 대한 카메라 이벤트 정보.
>
> -   화살표 : 전후 좌우 이동.
> -   delete, q : 좌회전
> -   insert, e : 우회전
> -   home : 확대
> -   end : 축소
> -   pageup : tilt 회전(상단)
> -   pagedown : tilt 회전(하단)

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                          |
| :--- | :------ | :------------------------------------------------------------------- |
| type | boolean | <p>true: 키보드 이벤트 활성화.<br>false: 키보드 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Keyboard Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_key)

{% endtab %}
{% tab title="Template" %}

```javascript
var vKeyEnable = Module.getControl().getKeyControlEnable();
// ... or ...
Module.getControl().setKeyControlEnable(false);
```

{% endtab %}
{% endtabs %}

### getKeyPanMode(), setKeyPanMode(type) → boolean

> 키보드의 화살표 입력으로 동작하는 이동(pan) 이벤트 발생 유무를 설정합니다.
>
> 키보드 이동 기본값은 true 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 이벤트 활성화.<br>false: 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Keyboard Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_key)

{% endtab %}
{% tab title="Template" %}

```javascript
var bPanEnable = Module.getControl().getKeyPanMode();
// ... or ...
Module.getControl().setKeyPanMode(false);
```

{% endtab %}
{% endtabs %}

### getKeyRotMode(), setKeyRotMode(type) → boolean

> 키보드의 Q, E delete, insert, pageup, pagedown으로 동작하는 회전(rotation) 이벤트 발생 유무를 설정합니다.
>
> 키보드 회전 기본값은 true 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 이벤트 활성화.<br>false: 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Keyboard Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_key)

{% endtab %}
{% tab title="Template" %}

```javascript
var bRotEnable = Module.getControl().getKeyRotMode();
// ... or ...
Module.getControl().setKeyRotMode(false);
```

{% endtab %}
{% endtabs %}

### getKeyZoomMode(), setKeyZoomMode(type) → boolean

> 키보드의 home, end으로 동작하는 확대, 축소(zoom) 이벤트 발생 유무를 설정합니다.
>
> 키보드 확대, 축소 기본값은 true 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 이벤트 활성화.<br>false: 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Keyboard Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_key)

{% endtab %}
{% tab title="Template" %}

```javascript
var bZoomEnable = Module.getControl().getKeyZoomMode();
// ... or ...
Module.getControl().setKeyZoomMode(true);
```

{% endtab %}
{% endtabs %}

### getMousePanMode(), setMousePanMode(type) → boolean

> 마우스 왼쪽 클릭 상태에서 마우스 드래그 동작시 발생하는 이동 이벤트 발생 유무를 설정합니다.
>
> 마우스 이동 기본값은 true 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 이벤트 활성화.<br>false: 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Mouse Button Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_mouse)

{% endtab %}
{% tab title="Template" %}

```javascript
var bPanEnable = Module.getControl().getMousePanMode();
// ... or ...
Module.getControl().setMousePanMode(false);
```

{% endtab %}
{% endtabs %}

### getMouseRotMode(), setMouseRotMode(type)→ boolean

> 마우스 오른쪽 클릭 상태에서 마우스 드래그 동작시 발생하는 회전 이벤트 발생 유무를 설정합니다.
>
> 마우스 회전 기본값은 true 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 이벤트 활성화.<br>false: 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Mouse Button Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_mouse)

{% endtab %}
{% tab title="Template" %}

```javascript
var bRotEnable = Module.getControl().getMouseRotMode();
// ... or ...
```

{% endtab %}
{% endtabs %}

### getMouseWheelDelta(), setMouseWheelDelta(value) → number

> 마우스 휠을 통해 지도 확대, 축소에 대한 이동 비율을 설정합니다.
>
> 입력 변수값(value)은 0 보다 큰 값을 입력합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description            |
| ----- | ------ | ---------------------- |
| value | number | 확대 축소 이동 비율값. |

-   Return

    -   number: 설정된 마우스 확대, 축소 이동 비율 값.

-   Sample
    -   function setMouseWheelDelta 참조.
    -   [Sandbox_Mouse Button Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_mouse)

{% endtab %}
{% tab title="Template" %}

```javascript
var wheelDelta = Module.getControl().getMouseWheelDelta();
// ... or ...
Module.getControl().setMouseWheelDelta(0.8);
```

{% endtab %}
{% endtabs %}

### getMouseWheelMode(), setMouseWheelMode(type) → boolean

> 마우스 휠을 통해 지도 확대, 축소에 대한 이동 방향을 반전 설정합니다.
>
> 이동 방향 기본값은 false 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 반전 이동 방향.<br>false: 기본 이동 방향.</p> |

-   Return

    -   true: 확대, 축소 시 반전 이동 방향으로 설정.
    -   false: 확대, 축소 시 기본 이동 방향으로 설정.

-   Sample
    -   function setMouseInvert 참조.
    -   [Sandbox_Mouse Wheel Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_mouse_wheel)

{% endtab %}
{% tab title="Template" %}

```javascript
var wheelInvert = Module.getControl().getMouseWheelMode();
// ... or ...
Module.getControl().setMouseWheelMode(true);
```

{% endtab %}
{% endtabs %}

### getMouseZoomMode(), setMouseZoomMode(type) → boolean

> 마우스 휠 동작시 발생하는 지도 확대, 축소 이벤트 발생 유무를 설정합니다.
>
> 마우스 확대, 축소 기본값은 true 입니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| type | boolean | <p>true: 이벤트 활성화.<br>false: 이벤트 비활성화.</p> |

-   Return

    -   true: 활성화 상태.
    -   false: 비활성화 상태.

-   Sample
    -   function setMouseOption 참조.
    -   [Sandbox_Mouse Button Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_mouse)

{% endtab %}
{% tab title="Template" %}

```javascript
var bZoomEnable = Module.getControl().getMouseZoomMode();
// ... or ...
Module.getControl().setMouseZoomMode(true);
```

{% endtab %}
{% endtabs %}

### getRotateSensitivity(), setRotateSensitivity(value) → number

> 카메라 회전시 회전 이동 비율을 설정합니다.
>
> 입력 변수값(value)은 1.0 ~ 10.0 사이값으로 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description       |
| ----- | ------ | ----------------- |
| value | number | 회전 이동 비율값. |

-   Return
    -   number: 설정된 카메라 회전 이동 비율값.

{% endtab %}
{% tab title="Template" %}

```javascript
// ... or ...
```

{% endtab %}
{% endtabs %}

### getTouchPanEnable(), setTouchPanEnable(type) → boolean

> 터치를 통한 카메라 이동 가능 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                          |
| :--- | :------ | :------------------------------------------------------------------- |
| type | boolean | <p>true: 터치 이동 활성화.<br>false: 터치 이동 비활성화.</p> |

-   Return
    -   true: 활성화 상태.
    -   false: 비활성화 상태.

{% endtab %}
{% tab title="Template" %}

```javascript
var vTouchPanEnable = Module.getControl().getTouchPanEnable();
// ... or ...
Module.getControl().setTouchPanEnable(false);
```

{% endtab %}
{% endtabs %}

### getTouchRotateEnable(), setTouchRotateEnable(type) → boolean

> 터치를 통한 카메라 회전 가능 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                          |
| :--- | :------ | :------------------------------------------------------------------- |
| type | boolean | <p>true: 터치 회전 활성화.<br>false: 터치 회전 비활성화.</p> |

-   Return
    -   true: 활성화 상태.
    -   false: 비활성화 상태.

{% endtab %}
{% tab title="Template" %}

```javascript
var vTouchRotateEnable = Module.getControl().getTouchRotateEnable();
// ... or ...
Module.getControl().setTouchRotateEnable(false);
```

{% endtab %}
{% endtabs %}

### getTouchZoomEnable(), setTouchZoomEnable(type) → boolean

> 터치를 통한 카메라 확대, 축소 가능 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                          |
| :--- | :------ | :------------------------------------------------------------------- |
| type | boolean | <p>true: 터치 확대, 축소 활성화.<br>false: 터치 확대, 축소 비활성화.</p> |

-   Return
    -   true: 활성화 상태.
    -   false: 비활성화 상태.

{% endtab %}
{% tab title="Template" %}

```javascript
var vTouchZoomEnable = Module.getControl().getTouchZoomEnable();
// ... or ...
Module.getControl().setTouchZoomEnable(false);
```

{% endtab %}
{% endtabs %}