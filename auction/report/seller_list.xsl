<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">

	<xsl:template match="/">
		<xsl:apply-templates select="seller-list"/>
	</xsl:template>

	<xsl:template match="seller-list">
		<document filename="example.pdf">
			<template pageSize="29.7cm,21cm" leftMargin="2.0cm" rightMargin="2.0cm" topMargin="2.0cm" bottomMargin="2.0cm" title="" author="Generated by Tiny ERP, Fabien Pinckaers" allowSplitting="20">
<!--
			<template pageSize="21m,29.7cm" leftMargin="2.0cm" rightMargin="2.0cm" topMargin="2.0cm" bottomMargin="2.0cm" title="" author="Generated by Tiny ERP, Fabien Pinckaers" allowSplitting="20">
-->
				<pageTemplate id="first">
					<pageGraphics>
						<drawRightString x="19.0cm" y="26.0cm"><xsl:value-of select="date"/></drawRightString>
					</pageGraphics>
					<frame id="list" x1="1.0cm" y1="1.0cm" width="27.7cm" height="19cm"/>
<!--
					<frame id="list" x1="2.0cm" y1="2.5cm" width="17.0cm" height="22.7cm"/>
-->
				</pageTemplate>
			</template>
			
			<stylesheet>
				<paraStyle name="name" fontName="Helvetica-Bold" fontSize="16" alignment="center"/>
				<paraStyle name="cost-name" fontName="Helvetica-BoldOblique" fontSize="10" alignment="RIGHT"/>
				<blockTableStyle id="products">
					 <blockAlignment value="RIGHT" start="2,0" stop="-1,-1"/>
					 <lineStyle kind="LINEBELOW" start="0,0" stop="-1,0"/>
					 <lineStyle kind="LINEABOVE" start="0,-1" stop="-1,-1"/>
					 <blockFont name="Helvetica-BoldOblique" size="12" start="0,0" stop="-1,0"/>
					 <blockValign value="TOP"/>
				</blockTableStyle>
			</stylesheet>
			
			<story>
				<xsl:apply-templates select="auctions"/>
			</story>
		</document>
	</xsl:template>

	<xsl:template match="auctions">
		<para style="name"><xsl:value-of select="title"/></para>

		<spacer length="1cm"/>

		<xsl:variable name="colWidths">
			<xsl:text>1.5cm,7.5cm,0.5cm,1.8cm</xsl:text>
			<xsl:for-each select="//cost-index">
				<xsl:text>,2cm</xsl:text>
			</xsl:for-each>
			<xsl:text>,2cm</xsl:text>
		</xsl:variable>
		
		<blockTable style="products" repeatRows="1"> 
			<xsl:attribute name="colWidths">
				<xsl:value-of select="$colWidths"/>
			</xsl:attribute>
			
			<tr>
				<td t="1">Inv.</td>
				<td t="1">Seller</td>
				<td t="1">#</td>
				<td t="1">Adj.</td>
				<xsl:apply-templates select="cost-index">
					<xsl:sort select="type" data-type="number"/>
					<xsl:sort select="name"/>
				</xsl:apply-templates>
				<td><para style="cost-name" t="1">To pay</para></td>
			</tr>
			<xsl:apply-templates select="sellers">
				<xsl:sort select="name" order="ascending"/>
<!--				<xsl:sort select="inventory" order="ascending"/>-->
			</xsl:apply-templates>
			<tr>
				<td><para><b t="1">Total:</b></para></td>
				<td/>
				<td><xsl:value-of select="count(sellers/product)"/></td>
				<td><xsl:value-of select="format-number(sum(sellers/product[price != '']/price), '#,##0.00')"/></td>
				<xsl:for-each select="//cost-index">
					<xsl:sort select="type" data-type="number"/>
					<xsl:sort select="name"/>
					<xsl:variable name="cost_type" select="type"/>
					<xsl:variable name="cost_id" select="id"/>
					<td><xsl:value-of select="format-number(sum(//sellers/cost[id=$cost_id and type=$cost_type]/amount), '#,##0.00')"/></td>
				</xsl:for-each>
				<td><xsl:value-of select="format-number(sum(sellers/product[price != '']/price) + sum(sellers/cost/amount), '#,##0.00')"/></td>
			</tr>
		</blockTable>
	</xsl:template>
	
	<xsl:template match="cost-index">
		<td><para style="cost-name"><xsl:value-of select="name"/></para></td>
	</xsl:template>

	<xsl:template match="sellers">
		<xsl:variable name="inv" select="inventory"/>
		<tr>
			<td><xsl:value-of select="inventory"/></td>
			<td><xsl:value-of select="name"/></td>
			<td><xsl:value-of select="count(product)"/></td>
			<td><xsl:value-of select="sum(product[price != '']/price)"/></td>
			<xsl:for-each select="//cost-index">
				<xsl:sort select="type" data-type="number"/>
				<xsl:sort select="name"/>
				<xsl:variable name="cost_type" select="type"/>
				<xsl:variable name="cost_id" select="id"/>
				<td><xsl:value-of select="//sellers[inventory=$inv]/cost[id=$cost_id and type=$cost_type]/amount"/></td>
			</xsl:for-each>
			<td><xsl:value-of select="sum(product[price != '']/price) + sum(cost/amount)"/></td>
		</tr>
	</xsl:template>

</xsl:stylesheet>