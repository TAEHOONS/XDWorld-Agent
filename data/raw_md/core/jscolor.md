---
description: 지도 내 ARGB 색상 처리를 위한 API 입니다.
---

# JSColor

> Module.JSColor() API를 생성합니다.
>
> JSColor 생성 시 기본값 ARGB(255, 255, 255, 255) 설정.

```javascript
var color = new Module.JSColor(255, 100, 100, 0); // ARGB
var color = new Module.JSColor(100, 100, 0); // RGB
var color = new Module.JSColor();
```

## properties

| Name | Type   | Description   |
| :--- | :----- | :------------ |
| a    | number | 투명도.       |
| r    | number | Red 색상값.   |
| g    | number | Green 색상값. |
| b    | number | Blue 색상값.  |

## Function

### getValue(index) → number

> 색상 값이 저장된 2진수 데이터를 10진수로 반환.
>
> 색상은 ARGB 순서대로 8bit씩 저장되어 있음(총 32bit).

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 10진수로 변환된 색상 데이터.

{% endtab %}
{% tab title="Template" %}

```javascript
var color = new Module.JSColor(255, 4, 32, 100);
var value = color.getValue(); // value : 4278460516
// Decimal 4278460516 in binary is 11111111000001000010000001100100
//  Binary 1111 1111 / 0000 0100 / 0010 0000 / 0110 0100
//   ARGB       255 /         4 /        32 /       100
```

{% endtab %}
{% endtabs %}

### setARGB(a, r, g, b)

> 색상 값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description   |
| :--- | :----- | :------------ |
| a    | number | 투명도.       |
| r    | number | Red 색상값.   |
| g    | number | Green 색상값. |
| b    | number | Blue 색상값.  |

{% endtab %}

{% tab title="Template" %}

```javascript
var color = new Module.JSColor();
color.SetARGB(255, 255, 0, 200);
```

{% endtab %}
{% endtabs %}

### setHexCode(hexCode)

> Hex 코드로 색상 값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description                                                                                  |
| :------ | :----- | :------------------------------------------------------------------------------------------- |
| hexCode | string | <p>#(00)(00)(00)(00)' 형태의 색상 코드.<br>숫자는 순서대로 A, r, g, b, 색상의 16진수 값.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var color = new Module.JSColor();
color.setHexCode("#FF002442");
```

{% endtab %}
{% endtabs %}
