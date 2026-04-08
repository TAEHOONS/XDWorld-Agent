---
description: 지도 내 네비게이션(난침반 UI) 기능을 설정 및 제어하기 위한 API 입니다.
---

# JSNavigationControl

> Module.getNavigation() API를 생성합니다.

```javascript
var navigation = Module.getNavigation();
```

## Function

### getPadding() → [JSVector2D](../core/jsvector2d.md)

> 나침반 Padding 값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   x : left Padding 설정값.
    -   y : top Padding 설정값.
-   Sample
    -   function getNavigationProperties 참조.
    -   [Sandbox_Map Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_map)

{% endtab %}
{% tab title="Template" %}

```javascript
var padding = Module.getNavigation().getPadding();
```

{% endtab %}
{% endtabs %}

### setPadding(number left, number top)

> 나침반 Padding 값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description      |
| ---- | ------ | ---------------- |
| left | number | left Padding 값. |
| top  | number | top Padding 값.  |

-   Sample
    -   function getNavigationProperties 참조.
    -   [Sandbox_Map Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_map)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getNavigation().setPadding(50, 50);
```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getNaviPos(), setNaviPos(align) → number

> 나침반 정렬을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                                                                  |
| ----- | ------ | ---------------------------------------------------------------------------- |
| align | number | [Navigation alignment type.](../etc/type-list.md#navigation-align-type-list) |

-   Return
    -   number: [navigation alignment type](../etc/type-list.md#navigation-align-type-list) 반환.
-   Sample
    -   function getNavigationProperties 참조.
    -   [Sandbox_Map Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_map)

{% endtab %}
{% tab title="Template" %}

```javascript
var naviAlign = Module.getNavigation().getNaviPos();
// ... or ...
Module.getNavigation().setNaviPos(Module.JS_NAVIGATION_LT);
```

{% endtab %}
{% endtabs %}

### getNaviVisible(), setNaviVisible(display) → number

> 나침반 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description                                                                     |
| ------- | ------ | ------------------------------------------------------------------------------- |
| display | number | [Navigation visibility type](../etc/type-list.md#navigation-visible-type-list). |

-   Return
    -   number: [navigation visibility type](../etc/type-list.md#navigation-visible-type-list) 반환.
-   Sample
    -   function getNavigationProperties 참조.
    -   [Sandbox_Map Control](https://sandbox.egiscloud.com/code/main.do?id=option_control_map)

{% endtab %}
{% tab title="Template" %}

```javascript
var naviDisplay = Module.getNavigation().getNaviVisible();
// ... or ...
Module.getNavigation().setNaviVisible(Module.JS_VISIBLE_AUTO);
```

{% endtab %}
{% endtabs %}
