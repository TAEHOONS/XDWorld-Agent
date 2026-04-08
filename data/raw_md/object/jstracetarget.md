---
description: 지도 내 경로 기능을 관리하기 위한 API 입니다.
---

# JSTraceTarget

> Module.createTraceTarget() API를 생성합니다.

```javascript
let trace = Module.createTraceTarget("ID");
```

## Function

### move(front, right, terrain)

> 객체를 이동합니다.
>
> 입력 변수값(front, right)으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                        |
| :------ | :------ | :------------------------------------------------- |
| front   | number  | 전후 이동 값(in meters).                           |
| right   | number  | 좌우 이동 값(in meters).                           |
| terrain | boolean | <p>true: 지형 곡면률 적용.<br>flase: 일반 이동.<p> |

{% endtab %}

{% tab title="Template" %}

```javascript
// Omission of traceTarget creation and connection process.
traceTarget.move(1.0, 1.0, true);
```

{% endtab %}
{% endtabs %}

### moveTarget(options)

> 객체를 이동합니다.
>
> [move](jstracetarget.md#move-front-right-terrain)와 달리, 6방향(전,후,좌,우,상,하)으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                                                        | Description |
| :-------- | :-------------------------------------------------------------------------- | :---------- |
| parameter | [JSTraceTarget.moveParameter](jstracetarget.md#jstracetarget.moveparameter) | 속성 정보.  |

{% endtab %}

{% tab title="Template" %}

```javascript
var move_front = 0.0;
var move_back = 0.0;
var move_left = 0.0;
var move_right = 0.0;
var move_up = 0.0;
var move_down = 0.0;

if (GLOBAL["KEY_PRESS_w"]) {
    move_front = 1.0;
} else if (GLOBAL["KEY_PRESS_s"]) {
    move_back = 1.0;
} else;

if (GLOBAL["KEY_PRESS_a"]) {
    move_left = 1.0;
} else if (GLOBAL["KEY_PRESS_d"]) {
    move_right = 1.0;
} else;

if (GLOBAL["KEY_PRESS_q"]) {
    move_down = 1.0;
} else if (GLOBAL["KEY_PRESS_e"]) {
    move_up = 1.0;
} else;

GLOBAL.TRACE_TARGET.moveTarget({
    front: move_front,
    back: move_back,
    left: move_left,
    right: move_right,
    down: move_down,
    up: move_up,
});
```

{% endtab %}
{% endtabs %}

### ReleaseObject() → boolean

> 연결된 객체를 해제 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 해제 성공.
    -   false: 해제 실패.

{% endtab %}

{% tab title="Template" %}

```javascript
// Omission of traceTarget creation and connection process.
traceTarget.ReleaseObject();
```

{% endtab %}
{% endtabs %}

### set(options)

> 대상 객체와 카메라 상태를 재설정합니다.
>
> 해당 객체는 [JSGhostSymbol](jsghostsymbol.md) 및 [JSPoint](jspoint.md)만 지원합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                      | Description |
| :-------- | :------------------------ | :---------- |
| object    | [JSObject](./jsobject.md) | 대상 객체.  |
| tilt      | number                    | 기울기.     |
| direction | number                    | 방향값.     |
| distance  | number                    | 거리값.     |

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### unionTargetToTerrain()

> 객체 이동시 지형 곡면률 적용 합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
// Omission of traceTarget creation and connection process.
traceTarget.unionTargetToTerrain();
```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getObject(), setObject(object) → [JSObject](./jsobject.md)

> 연결된 객체를 입력 변수값(object) 객체로 변경합니다.
>
> 해당 객체는 [JSGhostSymbol](jsghostsymbol.md) 및 [JSPoint](jspoint.md)만 지원하니다..
>
> 입력 변수값(object) 객체가 null이면 동작하지 않습니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                      | Description |
| ------ | ------------------------- | ----------- |
| object | [JSObject](./jsobject.md) | 객체.       |

-   Return
    -   [JSObject](jsobject.md): returned successfully.
    -   null : returned failed.

{% endtab %}
{% tab title="Template" %}

```javascript
// Omission of traceTarget creation and connection process.
traceTarget.getObject();
// ... or ...
// Omission of traceTarget creation and connection process.
traceTarget.setObject(object);
```

{% endtab %}
{% endtabs %}

### Type Definitions

#### JSTraceTarget.moveParameter

| Name  | Type   | Attributes | Default | Description              |
| ----- | ------ | ---------- | ------- | ------------------------ |
| front | number | optional   | 0.0     | 전방 이동값 (in meters). |
| back  | number | optional   | 0.0     | 후방 이동값 (in meters). |
| left  | number | optional   | 0.0     | 좌측 이동값 (in meters). |
| right | number | optional   | 0.0     | 우측 이동값 (in meters). |
| up    | number | optional   | 0.0     | 상승 이동값 (in meters). |
| down  | number | optional   | 0.0     | 하향 이동값 (in meters). |
